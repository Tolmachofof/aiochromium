from functools import partial

from ..base import Array, BaseType, String, Integer
from . import dom_base
from . import dom_events


class BoxModel(BaseType):

    @classmethod
    def from_response(cls, response_obj):
        if 'boxModel' in response_obj:
            return response_obj['boxModel']


class BackendNode(BaseType):

    def __init__(self, node_type, node_name, backend_node_id):
        self.node_type = node_type
        self.node_name = node_name
        self.backend_node_id = backend_node_id

    @classmethod
    def to_internal(cls, item, **kwargs):
        return cls(
            item['nodeType'], item['nodeName'], item['backendNodeId']
        )


class Node(BaseType):

    def __init__(
        self, node_id, backend_node_id, node_type, node_name, local_name,
        node_value, parent_id=None, child_node_count=None, children=None,
        attributes=None, document_url=None, base_url=None, public_id=None,
    ):
        self._node_id = node_id
        self.backend_node_id = backend_node_id,
        self.node_type = node_type
        self.node_name = node_name
        self.local_name = local_name
        self.node_value = node_value
        self.parent_id = parent_id
        self.child_node_count = child_node_count
        self.children = children or []
        self.attributes = attributes
        self.document_url = document_url
        self.base_url = base_url
        self.public_id = public_id

    @classmethod
    def to_internal(cls, response_obj, source=None, **kwargs):
        try:
            return cls(
                Integer.to_internal(response_obj.pop('nodeId')),
                Integer.to_internal(response_obj.pop('backendNodeId')),
                Integer.to_internal(response_obj.pop('nodeType')),
                String.to_internal(response_obj.pop('nodeName')),
                String.to_internal(response_obj.pop('localName')),
                String.to_internal(response_obj.pop('nodeValue')),
                parent_id=Integer.from_response(
                    response_obj.pop('parentId', None), blank=True
                ),
                child_node_count=Integer.from_response(
                    response_obj.pop('childNodeCount', None), blank=True
                ),
                children=Array.from_response(
                    response_obj.pop('children'), blank=True, default=[],
                    target=cls
                ),
                attributes=Array.from_response(
                    response_obj.pop('attributes'), blank=True, default=[],
                    target=String
                ),
                document_url=String.from_response(
                    response_obj.pop('documentURL', None), blank=True
                )
            )
        except KeyError:
            pass


    @property
    def node_id(self):
        return self._node_id
