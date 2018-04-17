from ..base import BaseType
from . import dom_base


class Node(BaseType):
    """
    The mirror object for represent the document's DOM node.

    You should use from_response method to create
    an instance(list of instances) from a raw response.
    """

    def __init__(self, executor, node_id, **kwargs):
        self._executor = executor
        self._node_id = node_id

    @classmethod
    def from_response(cls, executor, response_obj):
        if 'root' in response_obj:
            return cls(executor, response_obj['root']['nodeId'])
        elif 'nodeId' in response_obj:
            return cls(executor, response_obj['nodeId'])
        elif 'nodeIds' in response_obj:
            return [
                cls(executor, node_id) for node_id in response_obj['nodeIds']
            ]
        else:
            raise TypeError

    @property
    def node_id(self):
        return self._node_id

    async def query_selector(self, selector):
        """
        Get first element by css selector from current node.
        :param selector: string css selector.
        :return: Node instance or None if node was not found by selector.
        """
        return await self._executor.execute(
            dom_base.DOM.query_selector(self.node_id, selector)
        )

    async def query_selector_all(self, selector):
        """
        Get all elements by css selector from current node.
        :param selector: string css selector.
        :return: List Node instances or empty list is nodes were not found
        by css selector.
        """
        return await self._executor.execute(
            dom_base.DOM.query_selector_all(self.node_id, selector)
        )

    async def set_node_name(self, name):
        return await self._executor.execute(
            dom_base.DOM.set_node_name(self.node_id, name)
        )

    async def set_node_value(self, value):
        return await self._executor.execute(
            dom_base.DOM.set_node_value(self.node_id, value)
        )

    async def set_attribute_value(self, name, value):
        """
        Set attribute for current node.
        :param name: string attribute name.
        :param value: string attribute value.
        """
        return await self._executor.execute(
            dom_base.DOM.set_attribute_value(self.node_id, name, value)
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
            dom_base.DOM.set_attributes_as_text(self.node_id, text, name)
        )

    async def remove_attribute(self, name):
        return await self._executor.execute(
            dom_base.DOM.remove_attribute(self.node_id, name)
        )

    async def get_outer_html(self):
        return await self._executor.execute(
            dom_base.DOM.get_outer_html(self.node_id)
        )

    async def set_outer_html(self, outer_html):
        return await self._executor.execute(
            dom_base.DOM.set_outer_html(self.node_id, outer_html)
        )

    async def get_attributes(self):
        return await self._executor.execute(
            dom_base.DOM.get_attributes(self.node_id)
        )


class Attributes(BaseType):

    @classmethod
    def from_response(cls, executor, response_obj):
        return response_obj['attributes']


class OuterHTML(BaseType):

    @classmethod
    def from_response(cls, executor, response_obj):
        return response_obj['outerHTML']
