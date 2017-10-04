
import json
import collections
import asyncio
import websockets

from aiochromium.common import TabConnectionClosed


class MessagesStorage(collections.UserDict):
    pass


class Executor:
    
    RECV_TIMEOUT = 1
    
    def __init__(self):
        self._is_running = False
        self._msg_id = 0
        self.ws = None
        
        self._pending_tasks = set()
        self._accepted_tasks = {}
        
    @property
    def is_running(self):
        return self._is_running
        
    async def run(self, ws_addr):
        """
        Connects to web socket and runs the messages receive loop.
        """
        # TODO
        if self._is_running:
            raise
        self.ws = await websockets.connect(ws_addr)
        asyncio.ensure_future(self._start_recv_loop())
        
    async def stop(self):
        self._is_running = False
        await asyncio.sleep(0)
    
    async def _start_recv_loop(self):
        while True:
            if not self._is_running:
                self.ws = None
                break
            try:
                msg = await self.ws.recv()
                await self._accept(msg)
                await asyncio.sleep(0)
            except websockets.ConnectionClosed:
                raise TabConnectionClosed('Closed connection to tab.')
            
    async def _accept(self, msg):
        try:
            msg = json.loads(msg)
            msg_id = msg['id']
            # ignore message if nobody waits it.
            if msg_id in self._pending_tasks:
                self._pending_tasks.remove(msg_id)
                self._accepted_tasks[msg_id] = msg
        except Exception:
            pass
             
    async def execute(self, method, params=None, recv_retry=10):
        """
        Execute command in chrome tab.
        This method sends command to the chrome tab and starts
        the observe cycle that will return result or raise exception
        if result hasn't been accepted.
        :param method:
        :param params:
        :param recv_retry: is the max count the observe cycle passes.
        :return:
        """
        if not self.is_running:
            raise TabConnectionClosed('Closed connection to tab.')
        
        msg_id = self._msg_id
        self._msg_id += 1
        args = {
            'id': msg_id,
            'method': method,
            'params': params
        }
        self._pending_tasks.add(msg_id)
        await self.ws.send(json.dumps(args))
        
        # See accepted tasks while the message with msg_id hasn't been accepted
        # or recv_retry != 0
        while recv_retry:
            recv_retry -= 1
            result = self._accepted_tasks.get(msg_id)
            if result:
                return result
            await asyncio.sleep(1)
        # TODO
        raise Exception
