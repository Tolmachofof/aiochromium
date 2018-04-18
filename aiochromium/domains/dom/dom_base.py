from ..base import Domain, DomainMethod
from . import dom_types


class DOM(Domain):

    # Method, result wrapper_class, many
    _DESCRIBE_NODE = ('DOM.describeNode', dom_types.Node)
    _ENABLE = DomainMethod('DOM.enable', None)
    _DISABLE = DomainMethod('DOM.disable', None)
    _FOCUS = DomainMethod('DOM.focus', None)
    _GET_BOX_MODEL = DomainMethod('DOM.getBoxModel', None)
    _GET_FLATTENED_DOCUMENT = DomainMethod('DOM.getFlattenedDocument', None)
    _SET_FILE_INPUT_FILES = DomainMethod('DOM.setFileInputFiles', None)
    _GET_DOCUMENT = DomainMethod('DOM.getDocument', dom_types.Node)
    _REQUEST_CHILD_NODES = DomainMethod('DOM.requestChildNodes', None)
    _QUERY_SELECTOR = DomainMethod('DOM.querySelector', dom_types.Node)
    _QUERY_SELECTOR_ALL = DomainMethod('DOM.querySelectorAll', dom_types.Node)
    _SET_NODE_NAME = DomainMethod('DOM.setNodeName', dom_types.Node)
    _SET_NODE_VALUE = DomainMethod('DOM.setNodeValue', None)
    _REMOVE_NODE = DomainMethod('DOM.removeNode', None)
    _SET_ATTRIBUTE_VALUE = DomainMethod('DOM.setAttributeValue', None)
    _SET_ATTRIBUTES_AS_TEXT = DomainMethod('DOM.setAttributesAsText', None)
    _REMOVE_ATTRIBUTE = DomainMethod('DOM.removeAttribute', None)
    _GET_OUTER_HTML = DomainMethod('DOM.getOuterHTML', dom_types.OuterHTML)
    _SET_OUTER_HTML = DomainMethod('DOM.setOuterHTML', None)
    _REQUEST_NODE = DomainMethod('DOM.requestNode', dom_types.Node)
    _HIGHLIGHT_RECT = DomainMethod('DOM.highlightRect', None)
    _HIGHLIGHT_NODE = DomainMethod('DOM.highlightNode', None)
    _HIDE_HIGHLIGHT = DomainMethod('DOM.hideHighlight', None)
    _RESOLVE_NODE = DomainMethod('DOM.resolveNode', None)
    _GET_ATTRIBUTES = DomainMethod('DOM.getAttributes', dom_types.Attributes)
    _MOVE_TO = DomainMethod('DOM.moveTo', None)

    @classmethod
    def enable(cls):
        return cls.create_frame(cls._ENABLE)

    @classmethod
    def disable(cls):
        return cls.create_frame(cls._DISABLE)

    @classmethod
    def get_document(cls):
        return cls.create_frame(cls._GET_DOCUMENT)

    @classmethod
    def request_child_nodes(cls, node_id, depth=None):
        return cls.create_frame(
            cls._REQUEST_CHILD_NODES,
            {
                'nodeId': node_id,
                'depth': depth
            }
        )

    @classmethod
    def query_selector(cls, node_id, selector):
        return cls.create_frame(
            cls._QUERY_SELECTOR,
            {
                'nodeId': node_id,
                'selector': selector
            }
        )

    @classmethod
    def query_selector_all(cls, node_id, selector):
        return cls.create_frame(
            cls._QUERY_SELECTOR_ALL,
            {
                'nodeId': node_id,
                'selector': selector
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
    def remove_node(cls, node_id):
        return cls.create_frame(cls._REMOVE_NODE, {'nodeId': node_id})

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
    def remove_attribute(cls, node_id, name):
        return cls.create_frame(
            cls._REMOVE_ATTRIBUTE,
            {
                'nodeId': node_id,
                'name': name
            }
        )

    @classmethod
    def get_outer_html(cls, node_id):
        return cls.create_frame(cls._GET_OUTER_HTML, {'nodeId': node_id})

    @classmethod
    def set_outer_html(cls, node_id, outer_html):
        return cls.create_frame(
            cls._SET_OUTER_HTML,
            {
                'nodeId': node_id,
                'outerHTML': outer_html
            }
        )

    @classmethod
    def request_node(cls, object_id):
        return cls.create_frame(cls._REQUEST_NODE,{'objectId': object_id})

    @classmethod
    def highlight_rect(
        cls, x, y, width, height, color=None, outline_color=None
    ):
        return cls.create_frame(
            cls._HIGHLIGHT_RECT,
            {
                'x': x,
                'y': y,
                'width': width,
                'height': height,
                'color': color,
                'outlineColor': outline_color
            }
        )

    @classmethod
    def highlight_node(
        cls, highlight_config, node_id=None, backend_node_id=None,
        object_id=None
    ):
        return cls.create_frame(
            cls._HIGHLIGHT_NODE,
            {
                'highlightConfig': highlight_config,
                'nodeId': node_id,
                'backendNodeId': backend_node_id,
                'objectId': object_id
            }
        )

    @classmethod
    def hide_highlight(cls):
        return cls.create_frame(cls._HIDE_HIGHLIGHT)

    @classmethod
    def resolve_node(cls, node_id, object_group=None):
        return cls.create_frame(
            cls._RESOLVE_NODE,
            {
                'node_id': node_id,
                'objectGroup': object_group
            }
        )

    @classmethod
    def get_attributes(cls, node_id):
        return cls.create_frame(cls._GET_ATTRIBUTES, {'nodeId': node_id})

    @classmethod
    def move_to(cls, node_id, target_node_id, insert_before_node_id=None):
        return cls.create_frame(
            cls._MOVE_TO,
            {
                'nodeId': node_id,
                'targetNodeId': target_node_id,
                'insertBeforeNodeId': insert_before_node_id
            }
        )
