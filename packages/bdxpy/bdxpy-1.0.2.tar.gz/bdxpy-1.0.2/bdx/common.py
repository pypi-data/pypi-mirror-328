from requests import Response
from .types import DataNotFoundError, HttpRequestError, SecurityError
from enum import Enum

class HttpStatus(Enum):
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204
    MOVED_PERMANENTLY = 301
    FOUND = 302
    NOT_MODIFIED = 304
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    INTERNAL_SERVER_ERROR = 500
    NOT_IMPLEMENTED = 501
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503
    GATEWAY_TIMEOUT = 504

def _handle_http_error(resp : Response, key : any = None):
    if resp.status_code == HttpStatus.FORBIDDEN:
        raise SecurityError()
    elif resp.status_code != HttpStatus.NOT_FOUND or key is None:
        raise HttpRequestError(resp.status_code, resp.reason)
    else:
        raise DataNotFoundError(key, http_status = resp.status_code, http_message = resp.reason)
