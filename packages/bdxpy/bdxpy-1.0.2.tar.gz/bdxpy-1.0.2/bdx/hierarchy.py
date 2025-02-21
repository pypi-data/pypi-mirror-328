
from dataclasses import dataclass
from typing import Any, Self
from requests import Response
from .common import _handle_http_error
import dacite

@dataclass
class VirtualTreeNode:
    """
    Represents a node in BDX virtual hierarchy
    """
    _hierarchy : Any | None

    name : str
    type : str
    key : Any | None
    metadataType : str | None
    bdxType : str | None
    imageId : int | None
        
    keyPath : str
    namePath : str

    isLeaf : bool = False
    isDataPresent : bool = False

    @property
    def children(self) -> list[Self]:
        """
        Retrieves all children of this node
        """
        return self._hierarchy.children_by_key_path(self.keyPath)

class Hierarchy:
    """
    Facilitates node navigation in the virtual hierarchy tree
    """
    _parent : None
    _virtual_tree_api_root : str

    def __init__(self, parent) -> None:
        self._parent = parent
        self._virtual_tree_api_root = f"{self._parent.host_url}/bdx/rest/virtualTree"

    def _json_to_node_list(self, json : dict) -> list[VirtualTreeNode]:
        results = [ dacite.from_dict(data_class = VirtualTreeNode, data = node) for node in json ]
        for result in results:
            result._hierarchy = self

        return results

    @property
    def roots(self) -> list[VirtualTreeNode]:
        """
        Gets all root nodes of the BDX virtual hierarchy

        Returns
        -------
        list[VirtualTreeNode]
            Virtual hierarchy root nodes
        """
        resp : Response = self._parent.session.get(f"{self._virtual_tree_api_root}/roots")
        if not resp.ok:
            _handle_http_error(resp)

        return self._json_to_node_list(resp.json())
    
    def children_by_key_path(self, key_path : str) -> list[VirtualTreeNode]:
        """
        Gets the children of the node with the specified key path

        Parameters
        ----------
        key_path : str
            Key-based path to resolve

        Returns
        -------
        list[VirtualTreeNode]
            Child nodes of the specified virtual hierarchy node
        """
        resp : Response = self._parent.session.get(f"{self._virtual_tree_api_root}/children", params = { "keyPath" : key_path })
        if not resp.ok:
            _handle_http_error(resp)

        return self._json_to_node_list(resp.json())

