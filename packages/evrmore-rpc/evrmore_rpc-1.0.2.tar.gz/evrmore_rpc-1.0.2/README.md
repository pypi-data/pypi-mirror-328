# Evrmore RPC Client

A comprehensive Python client for interacting with Evrmore nodes via RPC and ZMQ interfaces. This module provides a clean, type-safe API for all Evrmore RPC commands with proper error handling and validation.

## Features

- 🚀 Complete implementation of all Evrmore RPC commands
- 📡 Real-time notifications via ZMQ with type-safe models
- 🔒 Type-safe request and response models using Pydantic
- 🛡️ Comprehensive error handling and logging
- 🧪 Command-line interfaces for testing RPC and ZMQ
- 📝 Extensive documentation and examples
- 🔧 Automatic configuration from evrmore.conf

## Installation

```bash
pip install evrmore_rpc
```

## Quick Start

### RPC Commands
```python
from evrmore_rpc import evrmore_rpc

# Create client (automatically reads evrmore.conf)
client = evrmore_rpc()

# Basic usage
block_count = client.getblockcount()
print(f"Current block height: {block_count}")

# Get asset information
asset_info = client.getassetdata("CREDITS")
print(f"Asset amount: {asset_info.amount}")

# Send EVR
txid = client.sendtoaddress("EXaMPLEaDDreSS123456789", 1.0)
print(f"Transaction sent: {txid}")

# Transfer assets
client.transfer("MYASSET", 100, "EXaMPLEaDDreSS123456789")
```

### ZMQ Notifications
```python
from evrmore_rpc.zmq import EvrmoreZMQ, HashTxNotification, HashBlockNotification

async def handle_notifications(notification):
    if isinstance(notification, HashTxNotification):
        print(f"New transaction: {notification.txid}")
    elif isinstance(notification, HashBlockNotification):
        print(f"New block: {notification.blockhash}")

# Create ZMQ client
zmq = EvrmoreZMQ()

# Subscribe to notifications
zmq.subscribe([b"hashtx", b"hashblock"], handle_notifications)

# Start listening
try:
    await zmq.start()
except KeyboardInterrupt:
    zmq.close()
```

## Configuration

The module automatically reads configuration from your `evrmore.conf` file. By default, it looks in:
1. The directory specified by the `EVRMORE_ROOT` environment variable
2. The default location (`~/.evrmore/evrmore.conf`)

Required settings in `evrmore.conf`:
```ini
# Core Settings (Required)
server=1
rpcuser=your_username
rpcpassword=your_password
rpcport=8819

# Optional Settings
rpcbind=127.0.0.1  # Default if not specified

# ZMQ Settings (for notifications)
zmqpubhashtx=tcp://127.0.0.1:28332
zmqpubhashblock=tcp://127.0.0.1:28332
zmqpubrawtx=tcp://127.0.0.1:28332
zmqpubrawblock=tcp://127.0.0.1:28332
zmqpubsequence=tcp://127.0.0.1:28332
```

## Command Line Interface

### RPC Commands
```bash
# Get current block count
evrmore_rpc getblockcount

# Get asset data
evrmore_rpc getassetdata CREDITS

# Get help for specific command
evrmore_rpc help getblock

# List all available commands
evrmore_rpc help
```

### ZMQ Monitor
```bash
# Monitor all ZMQ notifications
python3 -m evrmore_rpc.zmq

# Output example:
# [11:38:57] New transaction: 8ec3c9e86a10d04976249081c10661f0351931dbd9a2e6b98af4e10fbb914cd0
# [11:38:57] Raw transaction: 205 bytes
# [11:39:00] New block: 00000000003e584551ef457c1e194a0e60f86156b12d76b43bbd56d4db1111c4
```

## Security Considerations

### RPC Security
- Always use strong, unique credentials for `rpcuser` and `rpcpassword`
- Restrict RPC access:
  ```ini
  # Only allow local connections (recommended)
  rpcbind=127.0.0.1
  rpcallowip=127.0.0.1
  
  # If remote access is needed, use IP restrictions
  rpcallowip=192.168.1.0/24  # Allow specific network
  ```
- Use a firewall to restrict access to RPC port
- Consider using SSL/TLS for RPC connections (requires reverse proxy)

### ZMQ Security
- ZMQ endpoints should only bind to localhost unless remote access is needed
- Use proper network segmentation if remote ZMQ access is required
- Monitor ZMQ connections for unexpected behavior
- Consider implementing message authentication if using over untrusted networks

### Production Deployment
1. **Environment**:
   - Use dedicated service accounts
   - Implement proper file permissions
   - Use systemd or similar for process management

2. **Monitoring**:
   - Monitor RPC and ZMQ connection attempts
   - Set up logging for authentication failures
   - Monitor system resource usage

3. **Backup and Recovery**:
   - Regularly backup configuration
   - Document recovery procedures
   - Test failover scenarios

4. **Updates**:
   - Keep Evrmore node updated
   - Monitor security advisories
   - Update dependencies regularly

## Error Handling

The module provides specific error classes for different types of failures:

```python
from evrmore_rpc import evrmore_rpc, NodeConnectionError, NodeAuthError, EvrmoreError

client = evrmore_rpc()

try:
    result = client.getassetdata("NONEXISTENT")
except NodeConnectionError as e:
    print(f"Connection failed: {e}")
except NodeAuthError as e:
    print(f"Authentication failed: {e}")
except EvrmoreError as e:
    print(f"Evrmore error {e.code}: {e}")
```

## Integration Examples

### Blockchain Explorer Backend
```python
from evrmore_rpc import evrmore_rpc
from evrmore_rpc.zmq import EvrmoreZMQ, HashTxNotification, HashBlockNotification

class ExplorerBackend:
    def __init__(self):
        self.rpc = evrmore_rpc()
        self.zmq = EvrmoreZMQ()
        self.zmq.subscribe([b"hashtx", b"hashblock"], self.handle_notifications)
    
    async def handle_notifications(self, notification):
        if isinstance(notification, HashTxNotification):
            tx = self.rpc.getrawtransaction(notification.txid, True)
            await self.update_transaction(tx)
        elif isinstance(notification, HashBlockNotification):
            block = self.rpc.getblock(notification.blockhash)
            await self.update_block(block)
    
    async def start(self):
        await self.zmq.start()
```

### Wallet Address Monitor
```python
from evrmore_rpc.zmq import EvrmoreZMQ, RawTxNotification

class AddressMonitor:
    def __init__(self, addresses: List[str]):
        self.addresses = addresses
        self.zmq = EvrmoreZMQ()
        self.zmq.subscribe([b"rawtx"], self.check_transaction)
    
    async def check_transaction(self, notification):
        if isinstance(notification, RawTxNotification):
            # Decode transaction and check if it involves our addresses
            if any(addr in notification.txhex for addr in self.addresses):
                await self.process_relevant_transaction(notification)
    
    async def start(self):
        await self.zmq.start()
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 