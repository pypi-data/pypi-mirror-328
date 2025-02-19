from .common import (
    Header,
    Body,
    Message,
    HeaderProtocol,
    BodyProtocol,
    MessageProtocol,
    keys_extractor,
    Handler,
    default_client_logger
)
from typing import Callable, Coroutine, Hashable
import asyncio
import logging


class TCPClient:
    host: str
    port: int
    reader: asyncio.StreamReader
    writer: asyncio.StreamWriter
    header_class: type[HeaderProtocol]
    body_class: type[BodyProtocol]
    message_class: type[MessageProtocol]
    handlers: dict[Hashable, Handler]
    extract_keys: Callable[[MessageProtocol], list[Hashable]]
    logger: logging.Logger

    def __init__(
            self, host: str = "127.0.0.1", port: int = 8888,
            header_class: type[HeaderProtocol] = Header,
            body_class: type[BodyProtocol] = Body,
            message_class: type[MessageProtocol] = Message,
            handlers: dict[Hashable, Handler] = {},
            extract_keys: Callable[[MessageProtocol], list[Hashable]] = keys_extractor,
            logger: logging.Logger = default_client_logger
        ):
        self.host = host
        self.port = port
        self.header_class = header_class
        self.body_class = body_class
        self.message_class = message_class
        self.handlers = handlers
        self.extract_keys = extract_keys
        self.logger = logger

    def add_handler(
            self, key: Hashable,
            handler: Handler
        ):
        """Register a handler for a specific key. The handler must
            accept a MessageProtocol object as an argument and return
            MessageProtocol, None, or a Coroutine that resolves to
            MessageProtocol | None.
        """
        self.logger.info("Adding handler for key=%s", key)
        self.handlers[key] = handler

    def on(self, key: Hashable):
        """Decorator to register a handler for a specific key. The
            handler must accept a MessageProtocol object as an argument
            and return a MessageProtocol, None, or a Coroutine that
            resolves to a MessageProtocol or None.
        """
        def decorator(func: Handler):
            self.add_handler(key, func)
            return func
        return decorator

    async def connect(self):
        """Connect to the server."""
        self.logger.info("Connecting to %s:%d", self.host, self.port)
        self.reader, self.writer = await asyncio.open_connection(self.host, self.port)

    async def send(self, message: MessageProtocol):
        """Send a message to the server."""
        self.logger.info("Sending message to server...")
        self.writer.write(message.encode())
        await self.writer.drain()
        self.logger.info("Message sent to server")

    async def receive_once(self) -> MessageProtocol:
        """Receive a message from the server. If a handler was
            registered for the message key, the handler will be called
            with the message as an argument, and the result will be
            returned if it is not None; otherwise, the received message
            will be returned. If the message checksum fails, the message
            will be discarded and None will be returned.
        """
        self.logger.info("Receiving message from server...")
        data = await self.reader.readexactly(self.header_class.header_length())
        header = self.header_class.decode(data)
        body = await self.reader.readexactly(header.body_length)
        body = self.body_class.decode(body)
        msg = self.message_class(header=header, body=body)
        keys = self.extract_keys(msg)
        result = None

        if not msg.check():
            self.logger.error("Message checksum failed")
            return None

        self.logger.info("Message received from server")
        for key in keys:
            if key in self.handlers:
                self.logger.info("Calling handler for key=%s", key)
                handler = self.handlers[key]
                result = handler(msg)
                if isinstance(result, Coroutine):
                    result = await result
                break

        if result is not None:
            return result

        return msg

    async def receive_loop(self):
        """Receive messages from the server indefinitely. Use with
            asyncio.create_task() to run concurrently, then use
            task.cancel() to stop.
        """
        while True:
            try:
                await self.receive_once()
            except asyncio.CancelledError:
                self.logger.info("Receive loop cancelled")
                break
            except Exception as e:
                self.logger.error("Error in receive_loop", exc_info=True)
                break

    async def close(self):
        """Close the connection to the server."""
        self.logger.info("Closing connection to server...")
        self.writer.close()
        await self.writer.wait_closed()
        self.logger.info("Connection to server closed")

    def set_logger(self, logger: logging.Logger):
        """Replace the current logger."""
        self.logger = logger
