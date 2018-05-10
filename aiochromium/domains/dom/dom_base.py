from ..base import Array, BaseDomain, String, Integer
from .dom_types import BoxModel, Node


class DOM(BaseDomain):

    _DESCRIBE_NODE = 'DOM.describeNode'
    _DISABLE = 'DOM.disable'
    _ENABLE = 'DOM.enable'
    _FOCUS = 'DOM.focus'
    _GET_ATTRIBUTES = 'DOM.getAttributes'
    _GET_BOX_MODEL = 'DOM.getBoxModel'
    _GET_DOCUMENT = 'DOM.getDocument'
    _GET_FLATTENED_DOCUMENT = 'DOM.getFlattenedDocument'
    _GET_OUTER_HTML = 'DOM.getOuterHTML'
    _HIDE_HIGHLIGHT = 'DOM.hideHighlight'
    _HIGHLIGHT_NODE = 'DOM.highlightNode'
    _HIGHLIGHT_RECT = 'DOM.highlightRect'
    _MOVE_TO = 'DOM.moveTo'
    _QUERY_SELECTOR = 'DOM.querySelector'
    _QUERY_SELECTOR_ALL = 'DOM.querySelectorAll'
    _REMOVE_ATTRIBUTE = 'DOM.removeAttribute'
    _REMOVE_NODE = 'DOM.removeNode'
    _REQUEST_CHILD_NODES = 'DOM.requestChildNodes'
    _REQUEST_NODE = 'DOM.requestNode'
    _RESOLVE_NODE = 'DOM.resolveNode'
    _SET_ATTRIBUTE_VALUE = 'DOM.setAttributeValue'
    _SET_ATTRIBUTES_AS_TEXT = 'DOM.setAttributesAsText'
    _SET_FILE_INPUT_FILES = 'DOM.setFileInputFiles'
    _SET_NODE_NAME = 'DOM.setNodeName'
    _SET_NODE_VALUE = 'DOM.setNodeValue'
    _SET_OUTER_HTML = 'DOM.setOuterHTML'

    @classmethod
    def describe_node(
        cls, node_id=None, backend_node_id=None, object_id=None, depth=None,
        pierce=None
    ):
        return cls.create_frame(
            cls._DESCRIBE_NODE,
            {
                'nodeId': node_id,
                'backendNodeId': backend_node_id,
                'objectId': object_id,
                'depth': depth,
                'pierce': pierce
            },
            wrapper_class=Node(source='node')
        )

    @classmethod
    def disable(cls):
        return cls.create_frame(cls._DISABLE)

    @classmethod
    def enable(cls):
        return cls.create_frame(cls._ENABLE)

    @classmethod
    def focus(cls, node_id=None, backend_node_id=None, object_id=None):
        return cls.create_frame(
            cls._FOCUS,
            {
                'nodeId': node_id,
                'backendNodeId': backend_node_id,
                'objectId': object_id
            }
        )

    @classmethod
    def get_attributes(cls, node_id):
        return cls.create_frame(
            cls._GET_ATTRIBUTES,
            {
                'nodeId': node_id
            },
            wrapper_class=Array(source='attributes', target=String)
        )

    @classmethod
    def get_box_model(cls, node_id=None, backend_node_id=None, object_id=None):
        return cls.create_frame(
            cls._GET_BOX_MODEL,
            {
                'nodeId': node_id,
                'backendNodeId': backend_node_id,
                'objectId': object_id
            },
            wrapper_class=BoxModel(source='boxModel')
        )

    @classmethod
    def get_document(cls, depth=None, pierce=None):
        return cls.create_frame(
            cls._GET_DOCUMENT,
            {
                'depth': depth,
                'pierce': pierce
            },
            wrapper_class=Node(source='root')
        )

    @classmethod
    def get_flattened_document(cls, depth=None, pierce=None):
        return cls.create_frame(
            cls._GET_FLATTENED_DOCUMENT,
            {
                'depth': depth,
                'pierce': pierce
            },
            wrapper_class=Array(source='nodes', target=Node)
        )

    @classmethod
    def get_outer_html(
        cls, node_id=None, backend_node_id=None, object_id=None
    ):
        return cls.create_frame(
            cls._GET_OUTER_HTML,
            {
                'nodeId': node_id,
                'backendNodeId': backend_node_id,
                'objectId': object_id
            },
            wrapper_class=String(source='outerHTML')
        )

    @classmethod
    def hide_highlight(cls):
        return cls.create_frame(cls._HIDE_HIGHLIGHT)

    @classmethod
    def highlight_node(cls):
        return cls.create_frame(cls._HIGHLIGHT_NODE)

    @classmethod
    def highlight_rect(cls):
        return cls.create_frame(cls._HIGHLIGHT_RECT)

    @classmethod
    def move_to(cls, node_id, target_node_id, insert_before_node_id=None):
        return cls.create_frame(
            cls._MOVE_TO,
            {
                'nodeId': node_id,
                'targetNodeId': target_node_id,
                'insertBeforeNodeId': insert_before_node_id
            },
            wrapper_class=Integer(source='nodeId')
        )

    @classmethod
    def query_selector(cls, node_id, selector):
        return cls.create_frame(
            cls._QUERY_SELECTOR,
            {
                'nodeId': node_id,
                'selector': selector
            },
            wrapper_class=Integer(source='nodeId')
        )

    @classmethod
    def query_selector_all(cls, node_id, selector):
        return cls.create_frame(
            cls._QUERY_SELECTOR_ALL,
            {
                'nodeId': node_id,
                'selector': selector
            },
            wrapper_class=Array(source='nodeIds', target=Integer)
        )

    @classmethod
    def remove_attribute(cls, node_id, name):
        return cls.create_frame(
            cls._REMOVE_ATTRIBUTE,
            {
                'nodeId': node_id,
                'name': name
            }
        )

    @classmethod
    def remove_node(cls, node_id):
        return cls.create_frame(cls._REMOVE_NODE, {'nodeId': node_id})

    @classmethod
    def request_child_nodes(cls, node_id, depth=None, pierce=None):
        return cls.create_frame(
            cls._REQUEST_CHILD_NODES,
            {
                'nodeId': node_id,
                'depth': depth,
                'pierce': pierce
            }
        )

    @classmethod
    def request_node(cls, object_id):
        return cls.create_frame(
            cls._REQUEST_NODE, {'objectId': object_id},
            wrapper_class=Integer(source='nodeId')
        )

    # TODO
    @classmethod
    def resolve_node(
        cls, node_id=None, backend_node_id=None, object_group=None
    ):
        return cls.create_frame(
            cls._RESOLVE_NODE,
            {
                'node_id': node_id,
                'backendNodeId': backend_node_id,
                'objectGroup': object_group
            }
        )

    @classmethod
    def set_attribute_value(cls, node_id, name, value):
        return cls.create_frame(
            cls._SET_ATTRIBUTE_VALUE,
            {
                'nodeId': node_id,
                'name': name,
                'value': value
            }
        )

    @classmethod
    def set_attributes_as_text(cls, node_id, text, name=None):
        return cls.create_frame(
            cls._SET_ATTRIBUTES_AS_TEXT,
            {
                'nodeId': node_id,
                'text': text,
                'name': name
            }
        )

    @classmethod
    def set_file_input_files(
        cls, files, node_id=None, backend_node_id=None, object_id=None
    ):
        return cls.create_frame(
            cls._SET_FILE_INPUT_FILES,
            {
                'files': files,
                'nodeId': node_id,
                'backendNodeId': backend_node_id,
                'objectId': object_id
            }
        )

    @classmethod
    def set_node_name(cls, node_id, name):
        return cls.create_frame(
            cls._SET_NODE_NAME,
            {
                'nodeId': node_id,
                'name': name
            }
        )

    @classmethod
    def set_node_value(cls, node_id, value):
        return cls.create_frame(
            cls._SET_NODE_VALUE,
            {
                'nodeId': node_id,
                'value': value
            }
        )

    @classmethod
    def set_outer_html(cls, node_id, outer_html):
        return cls.create_frame(
            cls._SET_OUTER_HTML,
            {
                'nodeId': node_id,
                'outerHTML': outer_html
            }
        )
