from urllib.parse import ParseResult, urlparse, urlunparse
from nacl.public import PrivateKey, Box, PublicKey
from nacl.utils import random as naclRandom
from nacl.encoding import Base64Encoder
from requests.models import Response
from requests.sessions import Session
from requests.adapters import HTTPAdapter
from requests import Request, PreparedRequest
import uuid

from urllib3 import Retry
import base64

from .auth import Authenticator, CredentialType, UsernameAndPasswordCredential
from .types import AuthenticationError


class KeyExchange:
    id : str
    nonce : bytes
    private_key : PrivateKey
    foreign_nonce : bytes
    foreign_public_key : PublicKey


    def __init__(self, id : str, foreign_pub_key : PublicKey, foreign_nonce : bytes, my_private_key : PrivateKey, my_nonce : bytes) -> None:
        super().__init__()

        self.id = id
        self.foreign_public_key = foreign_pub_key
        self.foreign_nonce = foreign_nonce
        self.private_key = my_private_key
        self.nonce = my_nonce
    
class BDXAuthenticationAdapter(HTTPAdapter):

    def __init__(self, auth: Authenticator, session, pool_connections: int = 10, pool_maxsize: int = 10, max_retries: Retry | int | None = 0, pool_block: bool = False) -> None:
        super().__init__(pool_connections, pool_maxsize, max_retries, pool_block)
        self.auth = auth
        self.session = session

    def get_host_name(self, req, redirect_url):
        urlInfo = urlparse(redirect_url)
        if (urlInfo.hostname != None):
            return urlInfo.hostname
        else:
            return urlparse(req.url).hostname
        
        
    def authenticate(self, dest):
        self.session._bdx_version = None

        cred = self.auth.get_credential(CredentialType.USERNAME_AND_PASSWORD)
        if (isinstance(cred, UsernameAndPasswordCredential)):
            pass
        else:
            raise ValueError("Username and password credential expected")
        
        login_url = urlunparse(dest._replace(path="/bdx/unrestricted/rest/security/authenticate"))
        client_id = uuid.uuid4().bytes.hex()
        
        res = self.session.secure_post(login_url, json={
            "username": cred.username,
            "password": cred.password,
            "clientId": client_id
        })

        if not res.ok:
            if res.status_code == 403:
                raise AuthenticationError("Access denied.", res.status_code,
                                            cause = res.text if res.text is not None else res.reason)
            else:
                raise AuthenticationError("Login failed due to an HTTP error.", res.status_code,
                                            cause = res.text if res.text is not None else res.reason)
        else:
            response_json = res.json()

            auth_result = response_json["authenticationResult"]
            if auth_result is None:
                raise AuthenticationError("Login failed. Authentication result is not available.")
            
            login_result = auth_result["resultCode"]

            if login_result != "SUCCESS":
                raise AuthenticationError("Login denied. Check the login result for more information.", login_result=login_result)

            monitoring_summary_url = urlunparse(dest._replace(path="/bdx/unrestricted/rest/management/monitoring/summary"))
            res = self.session.get(monitoring_summary_url)
            if res.ok:
                monitoring_summary = res.json()
                if "deployedApplications" in monitoring_summary:
                    try:
                        for app in monitoring_summary["deployedApplications"]:
                            if "applicationName" in app and "applicationVersion" in app and app["applicationName"] == "BDXCore":
                                self.session._bdx_version = app["applicationVersion"]
                                break
                    except TypeError:
                        pass

    def build_response(self, req, resp):
        if resp.status in (301, 302, 303, 307, 308):

            org_url = urlparse(req.url)
            if org_url.path == "/bdx/site/logout":
                pass    # Fall through to the end, do not authenticate
            else:
                dest = self.session.get_full_redir_url(req.url, resp.headers['Location'])

                if (dest.path == "/bdx/site/login"):
                    super().build_response(req, resp) 
                    self.authenticate(dest)
                    req.prepare_cookies(self.session.cookies)
                    new_resp = self.send(req)
                    return new_resp

        elif hasattr(req, 'encrypted') and req.encrypted:

            encrypted = super().build_response(req, resp)
            decrypted = self.session.decrypt_response(req, encrypted)
            return decrypted
        
        return super().build_response(req, resp)    

class BDXSession(Session):
    _bdx_version : str | None = None

    def __init__(self, auth: Authenticator) -> None:
        super().__init__()
        auth_adapter = BDXAuthenticationAdapter(auth=auth, session=self)
        self.mount("http://", auth_adapter)
        self.mount("https://", auth_adapter)

    def get_full_redir_url(self, original_url : str, new_location : str) -> ParseResult:
        parsed_loc = urlparse(new_location)
        parsed_org = urlparse(original_url)

        new_host_name = parsed_loc.hostname
        new_port = parsed_loc.port

        if new_port is None:
            new_port = parsed_org.port

        if new_host_name is None or new_host_name == '':
            new_host_name = parsed_org.hostname

        if new_port is not None and new_host_name is None:
            new_host_name = parsed_org.hostname

        net_loc = new_host_name
        if new_port is not None:
            net_loc = net_loc + ':' + str(new_port)

        new_loc = parsed_loc._replace(netloc=net_loc)
        if new_loc.scheme is None or new_loc.scheme == '':
            new_loc = new_loc._replace(scheme=parsed_org.scheme)

        return new_loc

    def prepare_key_exchange(self, url):
        private_key = PrivateKey.generate()
        public_key = private_key.public_key
        nonce = naclRandom(Box.NONCE_SIZE)

        dest = urlparse(url)
        key_exchange_url = urlunparse(dest._replace(path="/bdx/unrestricted/rest/security/key-exchange"))

        key_exchange_data = {
            "algorithm": "x25519-xsalsa20-poly1305",
            "nonce": base64.b64encode(nonce).decode("utf-8"),
            "publicKey": public_key.encode(Base64Encoder).decode("utf-8")
        }

        ke_response = self.post(key_exchange_url, json=key_exchange_data)
        if not ke_response.ok:
            raise "Secure key exchange failed"

        respJson = ke_response.json()

        foreign_public_key = PublicKey(respJson["publicKey"], Base64Encoder)
        foreign_nonce = base64.b64decode(respJson["nonce"])

        key_exchange = KeyExchange(respJson["pkExchangeId"], foreign_public_key, foreign_nonce, private_key, nonce)

        return key_exchange
    
    def encrypt_request(self, req : Request) -> PreparedRequest:
        ke = self.prepare_key_exchange(req.url)
        box = Box(ke.private_key, ke.foreign_public_key)

        prep_req = self.prepare_request(req)
        new_body = box.encrypt(prep_req.body, ke.foreign_nonce, Base64Encoder).ciphertext.decode("utf-8")

        new_data = {
            "contentType": prep_req.headers["Content-Type"],
            "payload": new_body
        }

        prep_req.prepare_body(None, None, new_data)
        prep_req.headers["X-BDX-PK-Exchange-ID"] = ke.id
        prep_req.encrypted = True
        prep_req.key_exchange = ke

        return prep_req
    
    def decrypt_response(self, req : PreparedRequest, resp : Response) -> Response:
        json = resp.json()
        ke : KeyExchange = req.key_exchange
        box = Box(ke.private_key, ke.foreign_public_key)

        payload = box.decrypt(json["payload"], ke.nonce, Base64Encoder)
        resp._content = payload
        resp.headers['Content-Length'] = str(len(payload))

        return resp
    
    def secure_post(self, url, data=None, json=None, **kwargs):
        req = Request("POST", url, data=data, json=json)
        return self.send(self.encrypt_request(req))
    
    @property
    def bdx_version(self) -> str:
        return self._bdx_version
