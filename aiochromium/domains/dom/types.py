from .base import DOM
from ..base import BaseType


class Node(BaseType):

    def __init__(
        self, executor, node_id, node_type, node_name, local_name, node_value,
    ):
        self._executor = executor
        self._node_id = node_id

    @classmethod
    def from_response(cls, response_obj):
        pass

    @property
    def node_id(self):
        return self._node_id

    async def query_selector(self, selector):
        """
        Get first element by css selector in current node.
        :param selector: string css selector.
        :return: Node instance or None if node was not found by selector.
        """
        return await self._executor.execute(
            DOM.query_selector(self.node_id, selector)
        )

    async def query_selector_all(self, selector):
        return await self._executor.execute(
            DOM.query_selector_all(self.node_id, selector)
        )

    async def set_node_name(self, name):
        return await self._executor.execute(

        )

    async def set_node_value(self, value):
        pass