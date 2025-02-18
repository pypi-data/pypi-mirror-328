import asyncio
import threading
import time
from abc import ABC
from collections.abc import Callable
from typing import Any, TypeVar

import orjson
import websockets
from pydantic import BaseModel

import kevinbotlib.exceptions
from kevinbotlib.logger import Logger as _Logger


class BaseSendable(BaseModel, ABC):
    timeout: float | None = None
    data_id: str = "kevinbotlib.dtype.null"
    flags: list[str] = []

    def get_dict(self) -> dict:
        return {"timeout": self.timeout, "value": None, "did": self.data_id}


class IntegerSendable(BaseSendable):
    value: int
    data_id: str = "kevinbotlib.dtype.int"

    def get_dict(self) -> dict:
        data = super().get_dict()
        data["value"] = self.value
        return data


class BooleanSendable(BaseSendable):
    value: bool
    data_id: str = "kevinbotlib.dtype.bool"

    def get_dict(self) -> dict:
        data = super().get_dict()
        data["value"] = self.value
        return data


class StringSendable(BaseSendable):
    value: str
    data_id: str = "kevinbotlib.dtype.str"

    def get_dict(self) -> dict:
        data = super().get_dict()
        data["value"] = self.value
        return data


class FloatSendable(BaseSendable):
    value: float
    data_id: str = "kevinbotlib.dtype.float"

    def get_dict(self) -> dict:
        data = super().get_dict()
        data["value"] = self.value
        return data


class AnyListSendable(BaseSendable):
    value: list
    data_id: str = "kevinbotlib.dtype.list.any"

    def get_dict(self) -> dict:
        data = super().get_dict()
        data["value"] = self.value
        return data


class DictSendable(BaseSendable):
    value: dict
    data_id: str = "kevinbotlib.dtype.dict"

    def get_dict(self) -> dict:
        data = super().get_dict()
        data["value"] = self.value
        return data


class BinarySendable(BaseSendable):
    value: bytes
    data_id: str = "kevinbotlib.dtype.bin"

    def get_dict(self) -> dict:
        data = super().get_dict()
        data["value"] = self.value.decode("utf-8")
        return data


T = TypeVar("T", bound=BaseSendable)


class KevinbotCommServer:
    """WebSocket-based server for handling real-time data synchronization."""

    def __init__(self, host: str = "localhost", port: int = 8765) -> None:
        self.host: str = host
        self.port: int = port

        self.logger = _Logger()

        self.data_store: dict[str, dict[str, Any]] = {}
        self.clients: set[websockets.ServerConnection] = set()
        self.tasks = set()

    async def remove_expired_data(self) -> None:
        """Periodically removes expired data based on timeouts."""
        while True:
            current_time = time.time()
            expired_keys = [
                key
                for key, entry in self.data_store.items()
                if entry["data"]["timeout"] and entry["tsu"] + entry["data"]["timeout"] < current_time
            ]
            for key in expired_keys:
                del self.data_store[key]
                await self.broadcast({"action": "delete", "key": key})
            await asyncio.sleep(1)

    async def broadcast(self, message: dict[str, Any]) -> None:
        """Broadcasts a message to all connected clients."""
        if self.clients:
            msg = orjson.dumps(message)
            await asyncio.gather(*(client.send(msg) for client in self.clients))

    async def handle_client(self, websocket: websockets.ServerConnection) -> None:
        """Handles incoming WebSocket connections."""
        self.clients.add(websocket)
        self.logger.info(f"New client connected: {websocket.id}")
        try:
            await websocket.send(orjson.dumps({"action": "sync", "data": self.data_store}))
            async for message in websocket:
                msg = orjson.loads(message)
                if msg["action"] == "publish":
                    key = msg["key"]
                    tsc = time.time() if key not in self.data_store else self.data_store[key]["tsc"]
                    self.data_store[key] = {
                        "data": msg["data"],
                        "tsu": time.time(),
                        "tsc": tsc,
                    }
                    await self.broadcast({"action": "update", "key": key, "data": self.data_store[key]})
                elif msg["action"] == "delete" and msg["key"] in self.data_store:
                    del self.data_store[msg["key"]]
                    await self.broadcast({"action": "delete", "key": msg["key"]})
        except websockets.ConnectionClosed:
            pass
        finally:
            self.logger.info(f"Client disconnected: {websocket.id}")
            self.clients.remove(websocket)

    async def serve_async(self) -> None:
        """Starts the WebSocket server."""
        self.logger.info("Starting a new KevinbotCommServer")
        server = await websockets.serve(self.handle_client, self.host, self.port, max_size=2**48 - 1)
        task = asyncio.create_task(self.remove_expired_data())
        self.tasks.add(task)
        task.add_done_callback(self.tasks.discard)
        await server.wait_closed()

    def serve(self):
        asyncio.run(self.serve_async())


class KevinbotCommClient:
    """KevinbotLib WebSocket-based client for real-time data synchronization and communication."""

    def __init__(
        self,
        host: str = "localhost",
        port: int = 8765,
        on_update: Callable[[str, Any], None] | None = None,
        on_delete: Callable[[str], None] | None = None,
        on_connect: Callable[[], None] | None = None,
        on_disconnect: Callable[[], None] | None = None,
        *,
        auto_reconnect: bool = True,
        register_basic_types: bool = True,
    ) -> None:
        self._host = host
        self._port = port
        self.auto_reconnect = auto_reconnect

        self.logger = _Logger()

        self.data_store: dict[str, Any] = {}
        self.data_types: dict[str, type[BaseSendable]] = {}

        self.running = False
        self.websocket: websockets.ClientConnection | None = None
        self.loop = asyncio.new_event_loop()
        self.thread: threading.Thread | None = None

        self.on_update = on_update
        self.on_delete = on_delete
        self.on_connect = on_connect
        self.on_disconnect = on_disconnect

        if register_basic_types:
            self.register_type(BaseSendable)
            self.register_type(IntegerSendable)
            self.register_type(BooleanSendable)
            self.register_type(StringSendable)
            self.register_type(FloatSendable)
            self.register_type(AnyListSendable)
            self.register_type(DictSendable)

    @property
    def host(self):
        return self._host
    
    @host.setter
    def host(self, value: str):
        self._host = value
        if self.is_connected():
            self.disconnect()
            self.connect()

    @property
    def port(self):
        return self._port
    
    @port.setter
    def port(self, value: str):
        self._port = value
        if self.is_connected():
            self.disconnect()
            self.connect()

    def get_latency(self) -> float:
        return self.websocket.latency if self.websocket else float('inf')

    def register_type(self, data_type: type[BaseSendable]):
        self.data_types[data_type.model_fields["data_id"].default] = data_type
        self.logger.debug(
            f"Registered data type of id {data_type.model_fields['data_id'].default} as {data_type.__name__}"
        )

    def connect(self) -> None:
        """Starts the client in a background thread."""
        if self.running:
            self.logger.warning("Client is already running")
            return

        self.running = True
        self.thread = threading.Thread(target=self._run_async_loop, daemon=True)
        self.thread.start()

    def wait_until_connected(self, timeout: float = 5.0):
        start_time = time.time()
        while not self.websocket:
            if time.time() > start_time + timeout:
                msg = "The connection timed out"
                raise kevinbotlib.exceptions.HandshakeTimeoutException(msg)
            time.sleep(0.02)

    def is_connected(self):
        return not not self.websocket

    def disconnect(self) -> None:
        """Stops the client and closes the connection gracefully."""
        self.running = False
        if self.loop and self.loop.is_running():
            asyncio.run_coroutine_threadsafe(self._close_connection(), self.loop)


    def _run_async_loop(self) -> None:
        """Runs the async event loop in a separate thread."""
        asyncio.set_event_loop(self.loop)
        if not self.loop.is_running():
            self.loop.run_until_complete(self._connect_and_listen())
        else:
            asyncio.run_coroutine_threadsafe(self._connect_and_listen(), self.loop)

    async def _connect_and_listen(self) -> None:
        """Handles connection and message listening."""
        while self.running:
            try:
                async with websockets.connect(f"ws://{self._host}:{self._port}", max_size=2**48 - 1, ping_interval=1) as ws:
                    self.websocket = ws
                    self.logger.info("Connected to the server")
                    if self.on_connect:
                        self.on_connect()
                    await self._handle_messages()
            except (websockets.ConnectionClosed, ConnectionError, OSError) as e:
                self.logger.error(f"Unexpected error: {e!r}")
                self.websocket = None
                if self.auto_reconnect and self.running:
                    self.logger.warning("Can't connect to server, retrying...")
                    await asyncio.sleep(1)
                else:
                    break

    async def _handle_messages(self) -> None:
        """Processes incoming messages."""
        if not self.websocket:
            return
        try:
            async for message in self.websocket:
                data = orjson.loads(message)

                if data["action"] == "sync":
                    self.data_store = data["data"]
                elif data["action"] == "update":
                    key, value = data["key"], data["data"]
                    self.data_store[key] = value
                    if self.on_update:
                        self.on_update(key, value)
                elif data["action"] == "delete":
                    key = data["key"]
                    self.data_store.pop(key, None)
                    if self.on_delete:
                        self.on_delete(key)
        except orjson.JSONDecodeError as e:
            self.logger.error(f"Error processing messages: {e}")

    async def _close_connection(self) -> None:
        """Closes the WebSocket connection."""
        if self.websocket:
            await self.websocket.close()
            self.logger.info("Connection closed")
            if self.on_disconnect:
                self.on_disconnect()
            self.websocket = None

    def send(self, key: str, data: BaseSendable) -> None:
        """Publishes data to the server."""
        if not self.running or not self.websocket:
            self.logger.error(f"Cannot publish to {key}: client is not connected")
            return

        async def _publish() -> None:
            if not self.websocket:
                return
            message = orjson.dumps({"action": "publish", "key": key, "data": data.get_dict()})
            await self.websocket.send(message)

        asyncio.run_coroutine_threadsafe(_publish(), self.loop)

    def get(self, key: str, data_type: type[T], default: Any = None) -> T | None:
        """Retrieves stored data."""
        if key not in self.data_store:
            return None
        if self.data_store.get(key, default)["data"]["did"] != data_type.model_fields["data_id"].default:
            self.logger.error(
                f"Couldn't get value of {key}, requested value of id {data_type.model_fields['data_id'].default}, got one of {self.data_store.get(key, default)['data']['did']}"
            )
            return None

        return data_type(**self.data_store.get(key, default)["data"])

    def delete(self, key: str) -> None:
        """Deletes data from the server."""
        if not self.running or not self.websocket:
            self.logger.error("Cannot delete: client is not connected")
            return

        async def _delete() -> None:
            if not self.websocket:
                return
            message = orjson.dumps({"action": "delete", "key": key})
            await self.websocket.send(message)

        asyncio.run_coroutine_threadsafe(_delete(), self.loop)
