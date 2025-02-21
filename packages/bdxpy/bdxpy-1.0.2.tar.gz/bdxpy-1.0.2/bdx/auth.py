from abc import ABC, abstractmethod
from enum import Enum

class UsernameAndPasswordCredential:
    """
    A credential, which contains a username and a password
    """
    username : str
    password : str

    def __init__(self, username : str, password : str) -> None:
        """
        Initializes the credential

        Parameters
        ----------
        username : str
            Username to use for login
        password : str
            Password to use for login
        """
        self.username = username
        self.password = password

class MFACodeCredential:
    """
    A credential, which contains the Multi-Factor Authentication (MFA) code
    """
    code : str

class CredentialType(Enum):
    USERNAME_AND_PASSWORD = 0
    MFA_CODE = 1

class Authenticator(ABC):
    """
    A BDX authenticator
    """

    @abstractmethod
    def get_credential(self, credential_type : CredentialType) -> UsernameAndPasswordCredential | MFACodeCredential :
        pass

class UsernameAndPasswordAuthenticator(Authenticator):
    """
    A static authenticator, which uses username and password credentials
    """
    cred : UsernameAndPasswordCredential

    def __init__(self, username : str, password : str) -> None:
        """
        Initalizes the username/password authenticator

        Parameters
        ----------
        username : str
            Username to use for login
        password : str
            Password to use for login
        """
        super().__init__()
        self.cred = UsernameAndPasswordCredential(username, password)

    def get_credential(self, credential_type: CredentialType) -> UsernameAndPasswordCredential | MFACodeCredential:
        """
        Gets the login credential

        Parameters
        ----------
        credentialType : CredentialType
            Credential type to get

        Returns
        -------
        UsernameAndPasswordCredential | MFACodeCredential
            This method always returns a username/password credential

        Raises
        ------
        ValueError
            If an MFA credential is requested. This class only provides usernames and passwords
        """
        if credential_type != CredentialType.USERNAME_AND_PASSWORD:
            raise ValueError("This authenticator can only supply username and password credentials")
        return self.cred
    
