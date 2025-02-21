from .hierarchy import Hierarchy
from .buildings import Buildings
from .auth import Authenticator
from .sessions import BDXSession
from .trending import Trending
from .components import Components
from urllib.parse import urlparse

class BDX:
    """
    Represents a connection to the BDX platform server.
    """

    _session : BDXSession = None
    _host_url : str = None
    _authenticator : Authenticator = None
    _trending : Trending
    _components : Components
    _buildings : Buildings
    _hierarchy : Hierarchy

    def __init__(self, host_url, authenticator : Authenticator) -> None:
        """
        Creates a BDX connection

        Parameters
        ----------
        hostUrl : str
            Base URL of the BDX installation to connect to
        authenticator : Authenticator
            Authenticator to use when contacting the BDX server
        """

        parse_result = urlparse(host_url)
        self._host_url = f"{parse_result.scheme}://{parse_result.netloc}"
        self._authenticator = authenticator
        self._session = BDXSession(self._authenticator)
        self._trending = Trending(self)
        self._components = Components(self)
        self._buildings = Buildings(self)
        self._hierarchy = Hierarchy(self)

    def logout(self) -> None:
        """
        Terminates the currently active BDX session. If the user attempts another
        operation on this BDX object, a re-authentication sequence will be launched.
        """
        if self._session != None:
            self._session.get(f"{self._host_url}/bdx/site/logout")

    def __enter__(self):
        return self
        
    def __exit__(self, type, value, traceback):
        self.logout()
        return False
    
    @property
    def session(self) -> BDXSession:
        """
        Gets a reference to the underlying BDX session object

        Returns
        -------
        BDXSession
            The session object used for low-level server communication
        """
        return self._session
    
    @property
    def host_url(self) -> str:
        """
        Retrieves the host URL for which this server connection was created.

        Returns
        -------
        str
            BDX host URL
        """
        return self._host_url
    
    @property
    def trending(self) -> Trending:
        """
        Facilitates access to BDX trending functions

        Returns
        -------
        Trending
            An interface to BDX trending functions
        """
        return self._trending
    
    @property
    def components(self) -> Components:
        """
        Facilitates access to BDX component lookup functions

        Returns
        -------
        Components
            An interface to BDX component lookup functions
        """
        return self._components
    
    @property
    def buildings(self) -> Buildings:
        """
        Facilitates access to BDX building object lookup and retrieval functions

        Returns
        -------
        Buildings
            An interface to BDX building functions
        """
        return self._buildings
    
    @property
    def hierarchy(self) -> Hierarchy:
        """
        Facilitates access to BDX virtual hierarchy navigation functions
        

        Returns
        -------
        Hierarchy
            An interface to the hierarchy functions
        """
        return self._hierarchy

    @property
    def platform_version(self) -> str | None:
        """
        Gets the BDX platform version of the server this object is connected to.

        Returns
        -------
        str | None
            BDX version string or None if the server connection is unavailable
        """

        if self.session.bdx_version is None:

            # Run a simple ping call to trigger authentication and get the version field populated

            self.session.get(f"{self._host_url}/bdx/rest/session/ping")

        return self.session.bdx_version

