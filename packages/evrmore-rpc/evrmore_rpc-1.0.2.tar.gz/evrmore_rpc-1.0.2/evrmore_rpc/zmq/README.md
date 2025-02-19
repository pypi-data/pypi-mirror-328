# Evrmore ZMQ Client

This module provides a simple interface for subscribing to ZeroMQ notifications from an Evrmore node. It's designed to be easy to use while providing type-safe handling of notifications through Pydantic models.

## Quick Start

```python
from evrmore_rpc.zmq import EvrmoreZMQ

# Create ZMQ client (automatically loads config from ~/.evrmore/evrmore.conf)
zmq_client = EvrmoreZMQ()

# Define callback for transaction notifications
async def handle_transactions(notification):
    if notification.topic == b"hashtx":
        print(f"New transaction: {notification.txid}")
    elif notification.topic == b"rawtx":
        print(f"Raw transaction ({notification.size} bytes): {notification.txhex[:64]}...")

# Subscribe to transaction notifications
zmq_client.subscribe([b"hashtx", b"rawtx"], handle_transactions)

# Start listening (this will block until interrupted)
await zmq_client.start()
```

## Available Topics

The Evrmore node supports the following ZMQ notification topics:

- `hashtx`: Transaction hash notifications (32 bytes)
- `rawtx`: Raw transaction notifications (variable size)
- `hashblock`: Block hash notifications (32 bytes)
- `rawblock`: Raw block notifications (variable size)
- `sequence`: Chain reorganization notifications (36 bytes)

## Notification Models

All notifications are validated using Pydantic models:

### Base Notification
```python
class ZMQNotification(BaseModel):
    topic: bytes
    sequence: int
    body: bytes
```

### Transaction Notifications
```python
class HashTxNotification(ZMQNotification):
    topic: Literal[b"hashtx"]
    txid: str  # Hex-encoded transaction hash

class RawTxNotification(ZMQNotification):
    topic: Literal[b"rawtx"]
    txhex: str  # Hex-encoded raw transaction
    size: int   # Size in bytes
```

### Block Notifications
```python
class HashBlockNotification(ZMQNotification):
    topic: Literal[b"hashblock"]
    blockhash: str  # Hex-encoded block hash

class RawBlockNotification(ZMQNotification):
    topic: Literal[b"rawblock"]
    blockhex: str  # Hex-encoded raw block
    size: int      # Size in bytes
```

### Chain Reorganization Notifications
```python
class SequenceNotification(ZMQNotification):
    topic: Literal[b"sequence"]
    height: int      # Block height
    blockhash: str   # Hex-encoded block hash
```

## Configuration

The ZMQ client uses the same configuration as the Evrmore RPC client. By default, it looks for `evrmore.conf` in the following locations:

1. Path specified in `EVRMORE_ROOT` environment variable
2. Default location: `~/.evrmore/evrmore.conf`

Required ZMQ settings in `evrmore.conf`:
```ini
# Enable ZMQ notifications (at least one required)
zmqpubhashtx=tcp://127.0.0.1:28332
zmqpubrawtx=tcp://127.0.0.1:28332
zmqpubhashblock=tcp://127.0.0.1:28332
zmqpubrawblock=tcp://127.0.0.1:28332
zmqpubsequence=tcp://127.0.0.1:28332
```

## Advanced Usage

### Multiple Callbacks

You can register multiple callbacks for the same topics:

```python
# Transaction processing
zmq_client.subscribe([b"hashtx"], process_transaction)

# Transaction logging
zmq_client.subscribe([b"hashtx"], log_transaction)

# Block processing
zmq_client.subscribe([b"hashblock", b"rawblock"], process_block)
```

### Async and Sync Callbacks

The client supports both async and synchronous callbacks:

```python
# Async callback
async def async_handler(notification):
    await process_notification(notification)

# Sync callback
def sync_handler(notification):
    process_notification(notification)

# Both work the same way
zmq_client.subscribe([b"hashtx"], async_handler)
zmq_client.subscribe([b"hashtx"], sync_handler)
```

### Error Handling

The client includes built-in error handling and logging:

```python
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("evrmore_rpc.zmq")

# Errors in callbacks are caught and logged
def buggy_handler(notification):
    raise Exception("Something went wrong!")  # This won't crash the client

zmq_client.subscribe([b"hashtx"], buggy_handler)
```

### Clean Shutdown

The client can be properly shut down:

```python
try:
    await zmq_client.start()
except KeyboardInterrupt:
    zmq_client.close()
```

## Command-line Testing

The module includes a command-line interface for testing ZMQ notifications:

```bash
python3 -m evrmore_rpc.zmq
```

This will connect to the Evrmore node and display all incoming notifications in a human-readable format.

## Integration Examples

### Blockchain Explorer Backend
```python
class ExplorerBackend:
    def __init__(self):
        self.zmq_client = EvrmoreZMQ()
        self.zmq_client.subscribe([b"hashtx", b"hashblock"], self.handle_notifications)
    
    async def handle_notifications(self, notification):
        if isinstance(notification, HashTxNotification):
            await self.update_transaction(notification.txid)
        elif isinstance(notification, HashBlockNotification):
            await self.update_block(notification.blockhash)
    
    async def start(self):
        await self.zmq_client.start()
```

### Wallet Address Monitoring
```python
class AddressMonitor:
    def __init__(self, addresses: List[str]):
        self.addresses = addresses
        self.zmq_client = EvrmoreZMQ()
        self.zmq_client.subscribe([b"rawtx"], self.check_transaction)
    
    async def check_transaction(self, notification):
        if isinstance(notification, RawTxNotification):
            # Decode transaction and check if it involves our addresses
            if any(addr in notification.txhex for addr in self.addresses):
                await self.process_relevant_transaction(notification)
    
    async def start(self):
        await self.zmq_client.start()
``` 