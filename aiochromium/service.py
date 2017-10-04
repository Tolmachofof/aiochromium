
import json
from collections import AsyncIterator
import asyncio
import aiohttp

from .web_element import WebElement
from .common import ErrorProcessor
from .executor import Executor
from .domains import Page, DOM


class ChromeTab:
    """
    Wrapper for manage Chrome tab.
    """
    
    def __init__(self, web_socket_url, tab_id, url, title):
        self.web_socket_url = web_socket_url
        self.tab_id = tab_id
        self.url = url
        self.title = title
        self.command_executor = Executor(web_socket_url)
        
    @property
    async def document(self):
        node = await self._execute(DOM.GET_DOCUMENT)
        return WebElement(self, node['result']['root']['nodeId'], 'root')
    
    @classmethod
    async def create(cls, ws_url, tab_id, url, title):
        tab = cls(ws_url, tab_id, url, title)
        await tab._create_connection()
        return tab
    
    async def _create_connection(self):
        await self.command_executor.start()
    
    async def _execute(self, method, params=None):
        return await self.command_executor.execute(method, params)

    async def open(self, url):
        """
        Opens url in current tab.
        :param url: the page url that will be opened in current tab.
        :return: the WebElement instance.
        """
        await self.command_executor.execute(Page.NAVIGATE, {'url': url})
        return await self.document
    
    async def reload(self):
        return await self._execute(Page.RELOAD)

    async def close(self):
        pass


class TabsIterator(AsyncIterator):
    
    def __init__(self, tabs):
        self.tabs = tabs
        self._current_tab = 0
        
    async def __anext__(self):
        if self._current_tab < len(self.tabs):
            return self.tabs[self._current_tab]
        else:
            raise StopAsyncIteration
    

class RemoteChrome:
    """
    Base class for connect and manage Google Chrome browser
    with remote debugging interface.
    """
    
    def __init__(self, host, port):
        self.host = host
        self.port = port

    @property
    async def tabs(self):
        return await self._get_tabs()
    
    async def new_tab(self, url=None):
        tab = await self._manage_tabs(event='new')
        return await ChromeTab.create(tab['webSocketDebuggerUrl'], tab['id'],
                                      tab['url'], tab['title'])

    async def _manage_tabs(self, event=None):
        event = '/' + event if event is not None else ''
        path = 'http://{host}:{port}/json'.format(host=self.host,
                                                  port=self.port) + event
        async with aiohttp.ClientSession() as session:
            async with session.get(path) as resp:
                return json.loads(await resp.text())

    async def _get_tabs(self):
        tabs = []
        for tab in await self._manage_tabs():
            if tab['type'] == 'page':
                tabs.append(await ChromeTab.create(
                    tab['webSocketDebuggerUrl'],
                    tab['id'],
                    tab['url'],
                    tab['title']
                ))
        return tuple(tabs)

    async def __aiter__(self):
        return TabsIterator(await self._get_tabs())
        
    def __str__(self):
        return 'Chrome browser is on http://{host}:{port}'\
            .format(host=self.host, port=self.port)

    def __repr__(self):
        return 'RemoteChrome({host}, {port})'.format(host=self.host,
                                                     port=self.port)


class LocalChrome(RemoteChrome):
    """
    Base class for manage local Google Chrome browser.
    """
    
    def __init__(self, port, args):
        super().__init__(host='localhost', port=port)
        
    async def start(self):
        pass
    
    async def stop(self):
        tabs = await self.tabs



