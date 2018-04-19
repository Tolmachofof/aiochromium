from .domains.dom.dom_base import DOM
from .domains.dom.dom_events import DOMEvents
from .domains.dom.dom_types import Node


class WebElement:

    def __init__(self, executor):
        self._executor = executor


class DomElement(WebElement):

    def __init__(self, executor, node):
        super().__init__(executor)
        if isinstance(node, Node):
            self._node_id = node.node_id
        else:
            self._node_id = node

    @property
    def node_id(self):
        return self._node_id

    async def on_attribute_modified(self, name, value):
        return await self._executor.execute(
            DOMEvents.attribute_modified(self.node_id, name, value)
        )

    async def query_selector(self, selector):
        """
        Get first element by css selector from current node.
        :param selector: string css selector.
        :return: Node instance or None if node was not found by selector.
        """
        node_id = await self._executor.execute(
            DOM.query_selector(self.node_id, selector)
        )
        return self.__class__(self._executor, node_id)

    async def query_selector_all(self, selector):
        """
        Get all elements by css selector from current node.
        :param selector: string css selector.
        :return: List Node instances or empty list is nodes were not found
        by css selector.
        """
        node_ids = await self._executor.execute(
            DOM.query_selector_all(self.node_id, selector)
        )
        return [
            self.__class__(self._executor, node_id) for node_id in node_ids
        ]

    async def set_node_name(self, name):
        return await self._executor.execute(
            DOM.set_node_name(self.node_id, name)
        )

    async def set_node_value(self, value):
        return await self._executor.execute(
            DOM.set_node_value(self.node_id, value)
        )

    async def set_attribute_value(self, name, value):
        """
        Set attribute for current node.
        :param name: string attribute name.
        :param value: string attribute value.
        """
        return await self._executor.execute(
            DOM.set_attribute_value(self.node_id, name, value)
        )

    async def set_attributes_as_text(self, text, name=None):
        """
        Set attributes for current node from given text.
        :param text: string text with a number of attributes. HTML parser will
        parse this text.
        :param name: string an attribute name to replace with new attributes
        derived from text.
        """
        return await self._executor.execute(
            DOM.set_attributes_as_text(self.node_id, text, name)
        )

    async def remove_attribute(self, name):
        return await self._executor.execute(
            DOM.remove_attribute(self.node_id, name)
        )

    async def get_outer_html(self):
        return await self._executor.execute(
            DOM.get_outer_html(self.node_id)
        )

    async def set_outer_html(self, outer_html):
        return await self._executor.execute(
            DOM.set_outer_html(self.node_id, outer_html)
        )

    async def get_attributes(self):
        return await self._executor.execute(
            DOM.get_attributes(self.node_id)
        )
