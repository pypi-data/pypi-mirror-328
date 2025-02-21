from dataclasses import dataclass
from typing import Any
from requests import Response
from .types import Image, ResourceType
from .components import ComponentInstance, ComponentPath
from .common import _handle_http_error
import dacite

@dataclass
class BuildingZone:
    """
    Represents a building zone
    """
    componentInstanceId : int
    name : str
    exterior : bool
    description : str
    assignedComponents : list[ComponentInstance] | None
    hiddenComponentsPresent : bool | None
    scheduleId : int | None

    def __post_init__(self):
        if self.assignedComponents is None:
            self.assignedComponents = []
        
        if self.hiddenComponentsPresent is None:
            self.hiddenComponentsPresent = False


@dataclass
class Address:
    """
    Contains a building address
    """
    addressId : int
    addr1 : str
    addr2 : str
    city : str
    state : str
    zip : str
    country : str
    geoLat : str | None
    geoLong : str | None

@dataclass
class BuildingCategory:
    """
    Represents a building category (available via Manage Building Categories menu)
    """
    buildingCategoryId : int
    name : str
    description : str
    buildingIds : list[int]

@dataclass
class BuildingSummary:
    """
    A cut-down summary of building information
    """
    componentInstanceId : int
    name : str
    sqft : int | None
    occupancy : int | None
    address : Address | None
    smallIcon : Image | None
    largeIcon : Image | None
    yearBuilt : int | None
    siteId : str | None
    buildingCategory : BuildingCategory | None
    buildingComponentGroupId : int | None
    energyStarAccountId : int | None
    energyStarPropertyId : str | None
    scheduleId : int | None
    defaultWeatherId : int | None
    
    costRates : dict[ResourceType, float]
    ghgEmissionRates : dict[ResourceType, float]

    updatable : bool | None

    def __post_init__(self):
        if self.costRates is None :
            self.costRates = { }
        if self.ghgEmissionRates is None:
            self.ghgEmissionRates = { }
        if self.updatable is None:
            self.updatable = False

@dataclass
class BuildingPointFolder:
    """
    Represents a building point folder
    (available under Assigned Point Folders tab in the building management screen)
    """
    buildingPointFolderId : int
    folderPath : ComponentPath
    folderPathAlias : str

@dataclass
class Building(BuildingSummary):
    """
    A complete building definition
    """
    zones : list[BuildingZone]
    pressurePoint : ComponentPath | None
    pressureSetpoint : ComponentPath | None
    outdoorCO2Sensor : ComponentPath | None
    assignedComponents : list[ComponentInstance] | None
    assignedPointFolders : list[BuildingPointFolder] | None

    def __post_init__(self):
        if self.assignedComponents is None:
            self.assignedComponents = [ ]
        if self.assignedPointFolders is None:
            self.assignedPointFolders = [ ]
        return super().__post_init__()

def _pre_process_rates(rates: dict[str, str]) -> dict[ResourceType, float]:
    return { ResourceType(key): float(value) for key, value in rates.items() if value is not None }

class Buildings:
    """
    Provides access to building lookup and retrieval functions
    """
    _parent : None
    _building_api_root : str

    def __init__(self, parent) -> None:
        self._parent = parent
        self._building_api_root = f"{self._parent.host_url}/bdx/rest/management/buildings"

    def __call__(self, building_id : int | None = None) -> list[BuildingSummary] | Building:
        """
        Retrieves a list of buildings or the specified building

        Parameters
        ----------
        building_id : int | None, optional
            Building ID to retrieve. If this parameter is not provided, a list of
            building summaries is returned.

        Returns
        -------
        list[BuildingSummary] | Building
            If a building ID was provided, the specified building. Otherwise, a
            list of building summaries.

        Raises
        ------
        DataNotFoundError
            Specified building was not found
        HttpRequestError
            There was an error in HTTP communications with the server
        """
        return self.list() if building_id is None else self.by_id(building_id)

    def list(self) -> list[BuildingSummary]:
        """
        Retrieves a list of building summaries

        Returns
        -------
        list[BuildingSummary]
            A list of all building summaries accessible to the current user

        Raises
        ------
        HttpRequestError
            There was an error in HTTP communications with the server
        """
        resp : Response = self._parent.session.get(self._building_api_root)
        if not resp.ok:
            _handle_http_error(resp)

        config = dacite.Config(type_hooks = { dict[ResourceType, float]: lambda v: _pre_process_rates(v) })

        return [ dacite.from_dict(data_class = BuildingSummary, data = source, config = config) for source in resp.json() ]
    
    def by_id(self, building_id : int) -> Building:
        """
        Retrieves a building by its ID

        Parameters
        ----------
        building_id : int
            ID of the building to retrieve

        Returns
        -------
        Building
            Retrieved building

        Raises
        ------
        DataNotFoundError
            Specified building was not found
        HttpRequestError
            There was an error in HTTP communications with the server
        """
        resp : Response = self._parent.session.get(f'{self._building_api_root}/{building_id}')
        if not resp.ok:
            _handle_http_error(resp, key = building_id)

        config = dacite.Config(type_hooks = { dict[ResourceType, float]: lambda v: _pre_process_rates(v) })

        return dacite.from_dict(data_class = Building, data = resp.json(), config = config)
