
import asyncio
import collections
import functools
import json

import websockets

from .common import TabConnectionClosed


ChromeRequest = collections.namedtuple(
    'ChromeRequest', ['id', 'method', 'params']
)


class Executor:
    
    RECV_TIMEOUT = 1
    
    def __init__(self, loop=None):
        self._is_running = False
        self._uid = 0
        self.ws = None
        self._loop = loop if loop is not None else asyncio.get_event_loop()
        self._pending_tasks = {}
        
    @property
    def is_running(self):
        return self._is_running
        
    async def run(self, ws_addr):
        """
        Connects to web socket and runs the messages receive loop.
        """
        if not self._is_running:
            self._is_running = True
            self.ws = await websockets.connect(ws_addr)
            asyncio.ensure_future(self._start_recv())

    async def _start_recv(self):
        while self._is_running:
            try:
                msg = await self.ws.recv()
                await self._accept(msg)
                await asyncio.sleep(0)
            except websockets.ConnectionClosed:
                raise TabConnectionClosed('Closed connection to tab.')
        
    async def stop(self):
        self._is_running = False
            
    async def _accept(self, msg):
        try:
            msg = json.loads(msg)
            msg_id = msg['id']
            # ignore message if nobody waits it.
            if msg_id in self._pending_tasks:
                self._pending_tasks[msg_id].set_result(msg)
        except Exception:
            pass
             
    async def execute(self, method, params=None):
        """
        Execute command in chrome tab.
        This method sends command to the chrome tab and starts
        the observe cycle that will return result or raise exception
        if result hasn't been accepted.
        :param method:
        :param params:
        :return:
        """
        if not self.is_running:
            raise TabConnectionClosed('Closed connection to tab.')
        task_uid = self._create_uid()
        task = self._create_pending_task(task_uid)
        self._pending_tasks[task_uid] = task
        await self.ws.send(json.dumps(ChromeRequest(task_uid, method, params)))
        return task

    def _create_uid(self):
        self._uid += 1
        return self._uid

    def _create_pending_task(self, task_uid):
        task = self._loop.create_future()
        self._pending_tasks[task_uid] = task
        task.add_done_callback(
            functools.partial(self._on_task_done, task_uid)
        )
        return task

    def _on_task_done(self, task_uid, future):
        self._pending_tasks.pop(task_uid)
