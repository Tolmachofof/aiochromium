from ..base import Domain, DomainMethod


class DOMEvents(Domain):

    _ATTRIBUTE_MODIFIED = DomainMethod('DOM.attributeModified', None)
    _ATTRIBUTE_REMOVED = DomainMethod('DOM.attributeRemoved', None)
    _CHARACTER_DATA_MODIFIED = DomainMethod('DOM.characterDataModified', None)
    _CHILD_NODE_COUNT_UPDATED = 'DOM.childNodeCountUpdated'
    _CHILD_NODE_INSERTED = 'DOM.childNodeInserted'
    _CHILD_NODE_REMOVED = 'DOM.childNodeRemoved'
    _DOCUMENT_UPDATED = 'DOM.documentUpdated'
    _SET_CHILD_NODES = 'DOM.setChildNodes'

    @classmethod
    def attribute_modified(cls, node_id, name, value):
        return cls.create_frame(
            cls._ATTRIBUTE_MODIFIED,
            {
                'nodeId': node_id,
                'name': name,
                'value': value
            }
        )

    @classmethod
    def attribute_removed(cls, node_id, name):
        return cls.create_frame(
            cls._ATTRIBUTE_REMOVED,
            {
                'nodeId': node_id,
                'name': name
            }
        )

    @classmethod
    def character_data_modified(cls, node_id, character_data):
        return cls.create_frame(
            cls._CHARACTER_DATA_MODIFIED,
            {
                'nodeId': node_id,
                'characterData': character_data
            }
        )

    @classmethod
    def child_node_count_updated(cls, node_id, child_node_count):
        return cls.create_frame(
            cls._CHILD_NODE_COUNT_UPDATED,
            {
                'nodeId': node_id,
                'childNodeCount': child_node_count
            }
        )

    @classmethod
    def child_node_inserted(cls, parent_node_id, previous_node_id, node):
        return cls.create_frame(
            cls._CHILD_NODE_INSERTED,
            {
                'parentNodeId': parent_node_id,
                'previousNodeId': previous_node_id,
                'node': node
            }
        )

    @classmethod
    def child_node_removed(cls, parent_node_id, node_id):
        return cls.create_frame(
            cls._CHILD_NODE_REMOVED,
            {
                'parentNodeId': parent_node_id,
                'nodeId': node_id
            }
        )

    @classmethod
    def document_updated(cls):
        return cls.create_frame(cls._DOCUMENT_UPDATED)

    @classmethod
    def set_child_nodes(cls, parent_id, nodes):
        return cls.create_frame(
            cls._SET_CHILD_NODES,
            {
                'parentId': parent_id,
                'nodes': nodes
            }
        )
