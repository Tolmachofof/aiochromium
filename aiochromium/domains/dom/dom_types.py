from ..base import BaseType
from . import dom_base
from . import dom_events


class NodeId(BaseType):

    @classmethod
    def from_response(cls, response_obj):
        if 'nodeId' in response_obj:
            return int(response_obj['nodeId'])
        elif 'nodeIds' in response_obj:
            return [int(node_id) for node_id in response_obj['nodeIds']]


class BackendNodeId(BaseType):

    @classmethod
    def from_response(cls, response_obj):
        if 'backendNodeId' in response_obj:
            return int(response_obj['nodeId'])
        elif 'backendNodeIds' in response_obj:
            return [int(node_id) for node_id in response_obj['nodeIds']]


class BackendNode(BaseType):

    def __init__(self, node_type, node_name, backend_node_id):
        self.node_type = node_type
        self.node_name = node_name
        self.backend_node_id = backend_node_id

    @classmethod
    def from_response(cls, response_obj):
        if 'backendNode' in response_obj:
            return cls(
                response_obj['backendNode']['nodeType'],
                response_obj['backendNode']['nodeName'],
                response_obj['backendNode']['backendNodeId']
            )


class Node(BaseType):

    def __init__(
        self, executor, node_id, backend_node_id, node_type, node_name,
        local_name, node_value, parent_id=None, child_node_count=None,

    ):
        self._executor = executor
        self._node_id = node_id
        self.backend_node_id = backend_node_id
        self.node_type = node_type
        self.node_name = node_name
        self.local_name = local_name
        self.node_value = node_value

    @classmethod
    def from_response(cls, executor, response_obj):
        if 'root' in response_obj:
            return cls(
                executor, response_obj['root']['nodeId'],
                response_obj['root']['backendNodeId'],
                response_obj['root']['nodeType'],
                response_obj['root']['nodeName'],
                response_obj['root']['localName'],
                response_obj['root']['nodeValue'],

            )


    @property
    def node_id(self):
        return self._node_id


class Attributes(BaseType):

    @classmethod
    def from_response(cls, executor, response_obj):
        return response_obj['attributes']


class OuterHTML(BaseType):

    @classmethod
    def from_response(cls, executor, response_obj):
        return response_obj['outerHTML']
