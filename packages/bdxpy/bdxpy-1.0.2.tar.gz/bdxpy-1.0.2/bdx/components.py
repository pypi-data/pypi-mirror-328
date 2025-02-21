from dataclasses import dataclass
from typing import Any, Self
from requests import Response

from .common import HttpStatus, _handle_http_error
from .types import HttpRequestError, DataNotFoundError
import dacite

@dataclass
class ComponentPath:
    """
    Represents a path to a component within its associated data collection
    """
    componentPathId : int
    name : str
    fullPath : str
    parentPathId : int | None
    clientDataCollectionId : int
    currentComponentInstanceId : int | None
    dataCollectionName : str
    displayName : str | None
    displayFullPath : str | None

@dataclass
class ComponentInstance:
    """
    Represents a BDX component instance
    """
    _components : Any | None

    componentInstanceId : int
    path : ComponentPath
    entityTypeName : str
    templateType : str
    properties : dict[str, Any] | None
    subComponent : bool | None
    hierarchyRootComponent : bool | None
    
    parentName : str | None
    rootParentName : str | None

    def __post_init__(self):

        if self.subComponent is None:
            self.subComponent = False

        if self.hierarchyRootComponent is None:
            self.hierarchyRootComponent = False

        if self.parentName is None:
            self.parentName = ""

        if self.rootParentName is None:
            self.rootParentName = ""

    @property
    def child_components(self) -> list[Self]:
        """
        Gets the child components of this component.
        These are components, which exist on paths that are children of this
        component's path.

        Returns
        -------
        list[Self]
            Child components. There may be more than one component per child path,
            because the component history includes deleted components
        """
        return self._components.children_by_component(self)

class ComponentFilter:
    """
    An object, which specifies how to filter components for retrieval
    """
    path_keyword : str | None = None
    template_type : str | None = None
    only_subscribed : bool = False

class Components:
    """
    Provides access to BDX component lookup functions
    """
    _parent : None
    _comp_sel_api_root : None

    def __init__(self, parent) -> None:
        self._parent = parent
        self._comp_sel_api_root = f"{self._parent.host_url}/bdx/rest/componentSelection"

    def by_id(self, id : int) -> ComponentInstance:
        """
        Looks up the component by its ID

        Parameters
        ----------
        id : int
            Component ID to look up

        Returns
        -------
        ComponentInstance
            Component that matches the specified ID

        Raises
        ------
        DataNotFoundError
            Specified component ID was not found
        HttpRequestError
            There was an error in HTTP communications with the server
        """
        try:
            instances = self.by_ids([ id ])
        except HttpRequestError as ex:
            if ex.http_status == HttpStatus.NOT_FOUND:
                raise DataNotFoundError(id)
            else:
                raise
        
        if not instances:
            raise DataNotFoundError(id)
        else:
            return instances.pop(0)

    def by_ids(self, ids : list[int]) -> list[ComponentInstance]:
        """
        Looks up multiple components by their IDs

        Parameters
        ----------
        ids : list[int]
            Component IDs to match

        Returns
        -------
        list[ComponentInstance]
            A list of all matching components. If certain IDs did not match any
            components, there will be no matching objects in the result list

        Raises
        ------
        HttpRequestError
            There was an error in HTTP communications with the server
        """
        resp : Response = self._parent.session.get(f"{self._comp_sel_api_root}/search/by-ids", params = { "ids": ids })

        if not resp.ok:
            _handle_http_error(resp)
        
        result_list = resp.json()

        components = [ dacite.from_dict(data_class = ComponentInstance, data = v) for v in result_list ]
        for c in components:
            c._components = self

        return components

    def by_building(self, building_id : int, filter : ComponentFilter | None = None) -> list[ComponentInstance]:
        """
        Retrieves all components assigned to the specified building with additional filtering.
        Component assignment is performed in the Assigned Components tab of the building management screen

        Parameters
        ----------
        building_id : int
            Building ID for which to retrieve assigned components
        filter : ComponentFilter | None, optional
            An optional component filter. By default the filter is None, so
            no filtering is performed.

        Returns
        -------
        list[ComponentInstance]
            Matching components assigned to the specified building

        Raises
        ------
        HttpRequestError
            There was an error in HTTP communications with the server
        """
        resp : Response

        if filter is None:
            resp = self._parent.session.get(f"{self._comp_sel_api_root}/buildings/{building_id}/components")

            if not resp.ok:
                _handle_http_error(resp)
            
            result_list = resp.json()

            componentIds = [ v["componentInstanceId"] for v in result_list ]
            return self.by_ids(componentIds)

        else:
            params = {
                "onlySubscribed": "true" if filter.only_subscribed else "false",
            }

            if filter.path_keyword is not None:
                params["keyword"] = filter.path_keyword

            if filter.template_type is not None:
                params["templateType"] = filter.template_type

            resp = self._parent.session.get(f"{self._comp_sel_api_root}/search/by-building/{building_id}/by-keyword", params = params)

            if not resp.ok:
                _handle_http_error(resp)
            
            result_list = resp.json()

            components = [ dacite.from_dict(data_class = ComponentInstance, data = v) for v in result_list ]

            for c in components:
                c._components = self

            return components

    def by_data_collection(self, data_collection_id : int, filter : ComponentFilter, max_results : int = -1) -> list[ComponentInstance]:
        """
        Retrieves components from the specified data collection with filtering.

        Parameters
        ----------
        data_collection_id : int
            The ID of the data collection from which to retrieve components
        filter : ComponentFilter
            The filter to apply to components. At the very least, the pathKeyword
            attribute of the filter must be set to a non-empty string.
        max_results : int, optional
            Maximum number of matching components to return, by default -1. A negative
            value means no limit is set on the number of components. Negative values are
            not recommended due to performance and resource usage issues.

        Returns
        -------
        list[ComponentInstance]
            A list of matching components

        Raises
        ------
        ValueError
            A critical part of the filter was not provided
        HttpRequestError
            There was an error in HTTP communications with the server
        """
        if filter.path_keyword is None or filter.path_keyword == '':
            raise ValueError("Path keyword is required")
        
        parms = {
            "onlySubscribed": "true" if filter.only_subscribed else "false",
            "pageSize": 32767 if max_results <= 0 else max_results,
            "keyword": filter.path_keyword,
            "sortAscending": "true",
            "sortByName": "true"
        }

        if filter.template_type is not None:
            parms["templateType"] = filter.template_type

        resp : Response = self._parent.session.get(
            f"{self._comp_sel_api_root}/search/by-data-collection/{data_collection_id}/by-keyword", params = parms)
        
        if not resp.ok:
            _handle_http_error(resp)
        
        criteria_results = resp.json()
        
        components = [] if not "componentInstances" in criteria_results \
            else [ dacite.from_dict(data_class = ComponentInstance, data = v) for v in criteria_results["componentInstances"] ]
        
        for c in components:
            c._components = self

        return components
    
    def children_by_path(self, path : int | ComponentPath, type_filters : list[str] | None = None, only_subscribed : bool = False) -> list[ComponentInstance]:
        """
        Retrieves child components of the specified path

        Parameters
        ----------
        path : int | ComponentPath
            Either a path ID, or a complete path object for which children will be fetched
        type_filters : list[str] | None, optional
            Optionally filters the children by type name (e.g. "BooleanPoint", "VAV", etc.)
        only_subscribed : bool, optional
            If True, retrieves only subscribed components. The default is False

        Returns
        -------
        list[ComponentInstance]
            Retrieved component instances
        """
        path_id = path.componentPathId if isinstance(path, ComponentPath) else path

        parms = {
            "onlySubscribed": "true" if only_subscribed else "false",
        }

        if type_filters is not None:
            parms["filter"] = ",".join(type_filters)

        resp : Response = self._parent.session.get(
            f"{self._comp_sel_api_root}/componentSelectionDto/children/{path_id}", params = parms)
        
        if not resp.ok:
            _handle_http_error(resp)

        result_list = resp.json()

        instance_ids = [ int(c["componentInstanceId"]) for c in result_list ]

        return [] if len(instance_ids) == 0 else self.by_ids(instance_ids)
    
    def children_by_component(self, component : int | ComponentInstance, type_filters : list[str] | None = None, only_subscribed : bool = False) -> list[ComponentInstance]:
        """
        Retrieves child components of the specified component

        Parameters
        ----------
        component : int | ComponentInstance
            Parent component instance ID or the complete parent component
        type_filters : list[str] | None, optional
            Optionally filters the children by type name (e.g. "BooleanPoint", "VAV", etc.)
        only_subscribed : bool, optional
            If True, retrieves only subscribed components. The default is False

        Returns
        -------
        list[ComponentInstance]
            Retrieved component instances
        """
        if isinstance(component, ComponentInstance):
            if component.path is None:
                component = self.by_id(component.componentInstanceId)
        else:
            component = self.by_id(component)

        component_path_id = component.path.componentPathId

        return self.children_by_path(component_path_id, type_filters = type_filters, only_subscribed = only_subscribed)
