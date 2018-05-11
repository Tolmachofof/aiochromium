
import base64
import json
from collections import AsyncIterator
import asyncio
import aiohttp

#from aiochromium.web_element import WebElement
from aiochromium.common import ErrorProcessor
from aiochromium.executor import Executor
from aiochromium.domains import Page


class ChromeTab:
    """
    Wrapper for manage Chrome tab.
    """
    
    def __init__(self, tab_uid, url, title):
        self.tab_uid = tab_uid
        self.url = url
        self.title = title
        self._command_executor = Executor()
        
    # @property
    # async def document(self):
    #     node = await self.execute(DOM.GET_DOCUMENT)
    #     return WebElement(self, node['result']['root']['nodeId'], 'root')
    
    @classmethod
    async def create(cls, ws_addr, tab_id, url, title):
        tab = cls(tab_id, url, title)
        await tab.create_connection(ws_addr)
        return tab
    
    async def create_connection(self, ws_addr):
        await self._command_executor.run(ws_addr)

    async def take_screenshot(
        self, output, format='png', quality=None, clip=None, from_surface=True
    ):
        params = {}
        data = await self._command_executor.execute(Page.SCREENSHOT, )

    async def execute(self, frame):
        return await self._command_executor.execute(frame)

    async def open(self, url):
        """
        Opens url in current tab.
        :param url: the page url that will be opened in current tab.
        :return: the WebElement instance.
        """
        result = await self.execute(Page.navigate(url))
        frame_id = result['frameId']
        await self.execute(Page.frame_stopped_loading(frame_id))
    
    async def reload(self):
        return await self.execute(Page.reload())

    async def close(self):
        if self._command_executor.is_running:
            await self._command_executor.stop()


class TabsIterator(AsyncIterator):
    
    __slots__ = ('tabs', 'index')
    
    def __init__(self, tabs):
        self.tabs = tabs
        self.index = 0
        
    async def __anext__(self):
        if self.index < len(self.tabs):
            tab = self.tabs[self.index]
            self.index += 1
            return tab
        else:
            raise StopAsyncIteration
    

class Chrome:
    """
    Base class for connect and manage Google Chrome browser
    with remote debugging interface.
    """
    
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._tabs = []

    @property
    async def tabs(self):
        return tuple(self._tabs)
    
    async def new_tab(self):
        tab_info = await self._manage_tabs(event='new')
        new_tab = await ChromeTab.create(
            tab_info['webSocketDebuggerUrl'], tab_info['id'],
            tab_info['url'], tab_info['title']
        )
        self._tabs.append(new_tab)
        return new_tab

    async def _manage_tabs(self, event=None):
        event = '/' + event if event is not None else ''
        path = 'http://{host}:{port}/json'.format(host=self.host,
                                                  port=self.port) + event
        async with aiohttp.ClientSession() as session:
            async with session.get(path) as resp:
                return json.loads(await resp.text())

    async def __aiter__(self):
        return TabsIterator(await self.tabs)
        
    def __str__(self):
        return 'Chrome browser is on http://{host}:{port}'\
            .format(host=self.host, port=self.port)

    def __repr__(self):
        return 'RemoteChrome({host}, {port})'.format(host=self.host,
                                                     port=self.port)
from aiochromium.domains.dom import DOM

async def run_tab(chrome):
    tab = await chrome.new_tab()
    await tab.execute(Page.navigate('https://echo.msk.ru/'))
    #await asyncio.sleep(15)
    n = await tab.execute(DOM.get_document())
    print(n)
    print(n.node_name)
    print(n.children)
    print([i.children for i in n.children])
    print(await tab.execute(DOM.get_attributes(n.children[-1].node_id)))
    print(await tab.execute(DOM.get_outer_html(n.node_id)))


async def main():
    chrome = Chrome('127.0.0.1', 9222)
    await asyncio.wait(
        [run_tab(chrome) for _ in range(1)]
    )



l = asyncio.get_event_loop()
l.create_task(main())
l.run_forever()
