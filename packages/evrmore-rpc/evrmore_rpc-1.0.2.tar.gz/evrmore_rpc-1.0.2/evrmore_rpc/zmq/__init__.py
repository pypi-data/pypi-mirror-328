"""ZMQ module for subscribing to Evrmore node notifications

This module provides a simple interface for subscribing to ZeroMQ notifications from an Evrmore node.
It's designed to be easy to use while providing type-safe handling of notifications through Pydantic models.

Example:
    ```python
    from evrmore_rpc.zmq import EvrmoreZMQ

    # Create ZMQ client
    zmq_client = EvrmoreZMQ()

    # Define callback
    async def handle_transactions(notification):
        if isinstance(notification, HashTxNotification):
            print(f"New transaction: {notification.txid}")
        elif isinstance(notification, RawTxNotification):
            print(f"Raw transaction: {notification.size} bytes")

    # Subscribe to notifications
    zmq_client.subscribe([b"hashtx", b"rawtx"], handle_transactions)

    # Start listening
    await zmq_client.start()
    ```
"""
import zmq
import asyncio
import time
from typing import Dict, Callable, Any, Optional, List, Union, Awaitable, Literal as TypeLiteral
from pathlib import Path
import logging
from rich.logging import RichHandler
from pydantic import BaseModel

from evrmore_rpc.config import load_config

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)]
)
log = logging.getLogger("evrmore_rpc.zmq")

class ZMQNotification(BaseModel):
    """Base model for ZMQ notifications"""
    topic: bytes
    sequence: int
    body: bytes

class HashTxNotification(ZMQNotification):
    """Transaction hash notification with 32-byte transaction ID"""
    topic: TypeLiteral[b"hashtx"]
    txid: str = None  # Hex-encoded transaction hash

    def __init__(self, **data):
        super().__init__(**data)
        self.txid = self.body.hex()

class RawTxNotification(ZMQNotification):
    """Raw transaction notification with full transaction data"""
    topic: TypeLiteral[b"rawtx"]
    txhex: str = None  # Hex-encoded raw transaction
    size: int = None   # Size in bytes

    def __init__(self, **data):
        super().__init__(**data)
        self.txhex = self.body.hex()
        self.size = len(self.body)

class HashBlockNotification(ZMQNotification):
    """Block hash notification with 32-byte block hash"""
    topic: TypeLiteral[b"hashblock"]
    blockhash: str = None  # Hex-encoded block hash

    def __init__(self, **data):
        super().__init__(**data)
        self.blockhash = self.body.hex()

class RawBlockNotification(ZMQNotification):
    """Raw block notification with full block data"""
    topic: TypeLiteral[b"rawblock"]
    blockhex: str = None  # Hex-encoded raw block
    size: int = None     # Size in bytes

    def __init__(self, **data):
        super().__init__(**data)
        self.blockhex = self.body.hex()
        self.size = len(self.body)

class SequenceNotification(ZMQNotification):
    """Sequence notification for chain reorganization"""
    topic: TypeLiteral[b"sequence"]
    height: int = None      # Block height
    blockhash: str = None   # Hex-encoded block hash

    def __init__(self, **data):
        super().__init__(**data)
        self.height = int.from_bytes(self.body[:4], 'little')
        self.blockhash = self.body[4:].hex()

class ZMQHandler:
    """Internal ZMQ notification handler
    
    This class handles the low-level ZMQ socket management and notification processing.
    It's not meant to be used directly - use EvrmoreZMQ instead.
    """
    
    def __init__(self, endpoints: List[str]):
        """Initialize ZMQ handler with list of endpoints"""
        self.context = zmq.Context()
        self.endpoints = endpoints
        self.sockets: Dict[str, zmq.Socket] = {}
        self.callbacks: Dict[bytes, List[Callable]] = {}
        self.queue: asyncio.Queue = asyncio.Queue(maxsize=1000)
        self.loop = None
        self.running = True
        self.processor_task = None
        
        # Map topics to notification types
        self.notification_types = {
            b"hashtx": HashTxNotification,
            b"rawtx": RawTxNotification,
            b"hashblock": HashBlockNotification,
            b"rawblock": RawBlockNotification,
            b"sequence": SequenceNotification
        }
    
    def subscribe(self, topics: List[bytes], callback: Callable) -> None:
        """Subscribe to ZMQ notifications"""
        for topic in topics:
            log.info(f"Subscribing to topic: {topic}")
            
            # Add callback
            if topic not in self.callbacks:
                self.callbacks[topic] = []
            self.callbacks[topic].append(callback)
            
            # Create socket if needed
            for endpoint in self.endpoints:
                if endpoint not in self.sockets:
                    log.info(f"Creating new socket for endpoint: {endpoint}")
                    socket = self.context.socket(zmq.SUB)
                    socket.connect(endpoint)
                    self.sockets[endpoint] = socket
                
                # Subscribe to topic
                socket = self.sockets[endpoint]
                socket.setsockopt(zmq.SUBSCRIBE, topic)
                log.debug(f"Subscribed to {topic} on socket {endpoint}")
    
    async def _process_notifications(self):
        """Process notifications from the queue"""
        log.info("Starting notification processor")
        while True:
            try:
                message = await self.queue.get()
                topic, body, sequence = message
                
                # Create notification object
                notification_type = self.notification_types.get(topic, ZMQNotification)
                notification = notification_type(
                    topic=topic,
                    body=body,
                    sequence=int.from_bytes(sequence, 'little')
                )
                
                # Execute callbacks
                callbacks = self.callbacks.get(topic, [])
                for callback in callbacks:
                    try:
                        if asyncio.iscoroutinefunction(callback):
                            await callback(notification)
                        else:
                            callback(notification)
                    except Exception as e:
                        log.error(f"Error in callback: {e}", exc_info=True)
                
                self.queue.task_done()
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                log.error(f"Error processing notification: {e}", exc_info=True)
                await asyncio.sleep(1)
    
    def _handle_socket(self, socket: zmq.Socket, endpoint: str) -> None:
        """Handle messages from a ZMQ socket"""
        log.info(f"Starting socket handler for {endpoint}")
        
        while self.running:
            try:
                if socket.poll(timeout=100):  # Poll every 100ms
                    # Receive multipart message [topic, body, sequence]
                    message = socket.recv_multipart()
                    log.debug(f"Received message: topic={message[0]}, body={message[1].hex()}")
                    
                    # Add to queue
                    try:
                        self.loop.call_soon_threadsafe(
                            self.queue.put_nowait,
                            message
                        )
                    except asyncio.QueueFull:
                        log.warning("Queue full, dropping notification")
                
            except zmq.ZMQError as e:
                if self.running:
                    log.error(f"ZMQ error on {endpoint}: {e}", exc_info=True)
                    time.sleep(0.1)  # Small delay before retrying
            
            except Exception as e:
                if self.running:
                    log.error(f"Error receiving ZMQ message: {e}", exc_info=True)
                    time.sleep(0.1)  # Small delay before retrying
    
    async def start(self) -> None:
        """Start listening for ZMQ notifications"""
        log.info("Starting ZMQ handler")
        self.loop = asyncio.get_running_loop()
        self.running = True
        tasks = []
        
        # Start notification processor
        self.processor_task = asyncio.create_task(self._process_notifications())
        tasks.append(self.processor_task)
        
        # Start socket handlers
        for endpoint, socket in self.sockets.items():
            tasks.append(self.loop.run_in_executor(
                None,
                self._handle_socket,
                socket,
                endpoint
            ))
        
        log.info(f"Started {len(tasks)} tasks")
        await asyncio.gather(*tasks)
    
    def close(self) -> None:
        """Close all ZMQ sockets and stop processing"""
        log.info("Shutting down ZMQ handler")
        self.running = False
        
        # Close sockets
        for socket in self.sockets.values():
            socket.close()
        
        self.context.term()
        
        if self.processor_task and not self.processor_task.done():
            self.processor_task.cancel()
        
        log.info("ZMQ handler shutdown complete")

class EvrmoreZMQ:
    """High-level interface for Evrmore ZMQ notifications
    
    This class provides a simple interface for subscribing to ZMQ notifications from an Evrmore node.
    It automatically loads the configuration from evrmore.conf and manages the ZMQ connections.
    
    Example:
        ```python
        zmq_client = EvrmoreZMQ()
        zmq_client.subscribe([b"hashtx"], handle_transaction)
        await zmq_client.start()
        ```
    """
    
    def __init__(self, config_path: Optional[Path] = None):
        """Initialize ZMQ client
        
        Args:
            config_path: Optional path to evrmore.conf. If not provided,
                        the default location will be used.
        
        Raises:
            Exception: If no ZMQ endpoints are configured in evrmore.conf
        """
        # Load config
        raw_config = load_config(config_path)
        config_dict = raw_config.model_dump()
        
        # Get ZMQ endpoints
        endpoints = set()
        for key in ['zmqpubhashtx', 'zmqpubrawtx', 'zmqpubhashblock', 'zmqpubrawblock', 'zmqpubsequence']:
            if address := config_dict.get(key):
                endpoints.add(address)
        
        if not endpoints:
            raise Exception(
                "No ZMQ endpoints configured in evrmore.conf.\n"
                "Please add one or more of the following settings:\n"
                "  zmqpubhashtx=tcp://127.0.0.1:28332\n"
                "  zmqpubrawtx=tcp://127.0.0.1:28332\n"
                "  zmqpubhashblock=tcp://127.0.0.1:28332\n"
                "  zmqpubrawblock=tcp://127.0.0.1:28332\n"
                "  zmqpubsequence=tcp://127.0.0.1:28332"
            )
        
        # Initialize handler
        self._handler = ZMQHandler(list(endpoints))
    
    def subscribe(self, topics: List[bytes], callback: Callable) -> None:
        """Subscribe to ZMQ notifications
        
        Args:
            topics: List of topics to subscribe to (e.g., [b"hashtx", b"rawtx"])
            callback: Function to call when a notification is received.
                     Can be async or sync.
        """
        self._handler.subscribe(topics, callback)
    
    async def start(self) -> None:
        """Start listening for notifications
        
        This method will block until the client is stopped with close()
        or interrupted with Ctrl+C.
        """
        await self._handler.start()
    
    def close(self) -> None:
        """Stop listening and clean up resources"""
        self._handler.close()

__all__ = [
    'EvrmoreZMQ',
    'ZMQNotification',
    'HashTxNotification',
    'RawTxNotification',
    'HashBlockNotification',
    'RawBlockNotification',
    'SequenceNotification'
] 

