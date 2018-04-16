from ..base import Domain


class DOM(Domain):

    _ENABLE = 'DOM.enable'
    _DISABLE = 'DOM.disable'
    _GET_DOCUMENT = 'DOM.getDocument'
    _REQUEST_CHILD_NODES = 'DOM.requestChildNodes'
    _QUERY_SELECTOR = 'DOM.querySelector'
    _QUERY_SELECTOR_ALL = 'DOM.querySelectorAll'
    _SET_NODE_NAME = 'DOM.setNodeName'
    _SET_NODE_VALUE = 'DOM.setNodeValue'
    _REMOVE_NODE = 'DOM.removeNode'
    _SET_ATTRIBUTE_VALUE = 'DOM.setAttributeValue'
    _SET_ATTRIBUTES_AS_TEXT = 'DOM.setAttributesAsText'
    _REMOVE_ATTRIBUTE = 'DOM.removeAttribute'
    _GET_OUTER_HTML = 'DOM.getOuterHTML'
    _SET_OUTER_HTML = 'DOM.setOuterHTML'
    _REQUEST_NODE = 'DOM.requestNode'
    _HIGHLIGHT_RECT = 'DOM.highlightRect'
    _HIGHLIGHT_NODE = 'DOM.highlightNode'
    _HIDE_HIGHLIGHT = 'DOM.hideHighlight'
    _RESOLVE_NODE = 'DOM.resolveNode'
    _GET_ATTRIBUTES = 'DOM.getAttributes'
    _MOVE_TO = 'DOM.moveTo'

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
