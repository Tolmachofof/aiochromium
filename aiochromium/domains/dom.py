from .base import Domain, RequestFrame


class DOM(Domain):

    _ENABLE = 'DOM.enable'
    _DISABLE = 'DOM.disable'
    _GET_DOCUMENT = 'DOM.getDocument'
    _REQUEST_CHILD_NODES = 'DOM.requestChildNodes'
    _QUERY_SELECTOR = 'DOM.querySelector'

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


