
import asyncio
import aiohttp

from .domains import DOM


class WebElement:
    
    def __init__(self, chrome_tab, element_id, parent_id):
        self.chrome_tab = chrome_tab
        self._id = element_id
        self._parent_id = parent_id
        
    @property
    async def is_exist(self):
        return True
    
    @property
    async def outer_html(self):
        result = await self.chrome_tab._execute(DOM.GET_OUTER_HTML,
                                                {'nodeId': self._id})
        return result['result']['outerHTML']
    
    @property
    async def text(self):
        result = await  self.chrome_tab._execute('DOM.getAttributes',
                                                 {'nodeId': self._id})
        print(result)
        return result
    
    async def find_by_selector(self, selector):
        result = await self.chrome_tab._execute('DOM.querySelector',
                                                {'nodeId': self._id,
                                                 'selector': selector})
        if 'params' in result:
            return WebElement(self.chrome_tab, result['params']['nodeId'],
                              result['params']['parentId'])
        else:
            #TODO raise
            pass
        
    async def set_attribute(self, name, value):
        await self.chrome_tab._execute(DOM.SET_ATTRIBUTE,
                                       {'nodeId': self._id,
                                        'name': name,
                                        'value': value})
    
    def __str__(self):
        return 'Web element node id: {node_id}'.format(node_id=self._id)