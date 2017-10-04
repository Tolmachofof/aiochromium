
import json
import collections
import asyncio
import websockets

from aiochromium.common import TabConnectionClosed


class MessagesStorage(collections.UserDict):
    pass


class Executor:
    
    RECV_TIMEOUT = 1
    
    def __init__(self, web_sock):
        self._loop = asyncio.get_event_loop()
        self._msg_id = 0
        self._web_sock = web_sock
        self.ws = None
        
        self._pending_tasks = set()
        self._accepted_tasks = {}
        
        self._stopping = False
        
    async def start(self):
        """
        Connects to web socket and runs the messages receive loop.
        """
        self.ws = await websockets.connect(self._web_sock) if self.ws is None \
            else self.ws
        loop = asyncio.get_event_loop()
        loop.create_task(self._start_recv_loop())
        
    async def stop(self):
        self._stopping = True
    
    async def _start_recv_loop(self):
        while True:
            if self._stopping:
                break
            try:
                msg = await self.ws.recv()
                await self._accept(msg)
                await asyncio.sleep(0)
            except websockets.ConnectionClosed as exc:
                raise TabConnectionClosed('Closed connection to tab: {0}'
                                          .format(self._web_sock), exc)
            
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
        if self._stopping:
            raise TabConnectionClosed('Closed connection to tab: {0}'
                                      .format(self._web_sock))
        
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
