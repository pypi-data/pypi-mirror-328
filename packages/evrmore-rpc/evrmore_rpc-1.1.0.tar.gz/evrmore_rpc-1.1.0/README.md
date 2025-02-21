# evrmore-rpc

A typed Python wrapper for evrmore-cli commands with ZMQ support.

## Quick Start

```bash
# Install the package
pip install evrmore-rpc

# Basic usage
from evrmore_rpc import EvrmoreRPCClient

# Initialize client
client = EvrmoreRPCClient()

# Get blockchain info
info = client.getblockchaininfo()
print(f"Current block height: {info.blocks}")

# List assets
assets = client.listassets()
print(f"Found {len(assets)} assets")
```

## Features

- ✨ Full type hints for all evrmore-cli commands
- 🎨 Rich terminal output formatting
- 🖥️ Command-line interface
- 🔍 Python API with autocomplete support
- ⚡ ZMQ support for real-time notifications
- 📚 Interactive examples and tools

## Requirements

- Python 3.8 or higher
- evrmore-cli installed and accessible in your PATH
- ZMQ support in your Evrmore node (optional)

## Installation

```bash
# Basic installation
pip install evrmore-rpc

# With development tools
pip install evrmore-rpc[dev]
```

## Usage Examples

### Command Line Interface

```bash
# Get blockchain info
evrmore-rpc getblockchaininfo

# Get block by hash
evrmore-rpc getblock "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"

# Get JSON output
evrmore-rpc --json getblockcount
```

### Python API

```python
from evrmore_rpc import EvrmoreRPCClient

# Initialize the client
client = EvrmoreRPCClient()

# Get block by hash
block = client.getblock(
    "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"
)
print(f"Block timestamp: {block.time}")

# Issue an asset
result = client.issue(
    "MYASSET",
    1000,
    "EVRxxxxxxxxxxxxxxxxxxxxx",
    "EVRxxxxxxxxxxxxxxxxxxxxx"
)
print(f"Asset created with txid: {result}")
```

### ZMQ Support

Enable ZMQ in your `evrmore.conf`:

```conf
zmqpubhashtx=tcp://127.0.0.1:28332
zmqpubrawtx=tcp://127.0.0.1:28332
zmqpubhashblock=tcp://127.0.0.1:28332
zmqpubrawblock=tcp://127.0.0.1:28332
zmqpubsequence=tcp://127.0.0.1:28332
```

Use the ZMQ client:

```python
from evrmore_rpc.zmq.client import EvrmoreZMQClient

# Create ZMQ client
client = EvrmoreZMQClient()

# Handle new transactions
@client.on_transaction
async def handle_transaction(notification):
    print(f"New transaction: {notification.hex}")

# Start receiving notifications
await client.start()
```

## Configuration

Configure through command line:
```bash
evrmore-rpc --datadir ~/.evrmore --rpcuser myuser --rpcpassword mypass getinfo
```

Or in Python:
```python
client = EvrmoreRPCClient(
    datadir="~/.evrmore",
    rpcuser="myuser",
    rpcpassword="mypass",
    rpcport=8819
)
```

## Example Applications

The package includes several example applications:

- `blockchain_explorer`: Real-time block and transaction viewer
- `asset_monitor`: Track asset creation and transfers
- `wallet_tracker`: Monitor wallet balances and transactions
- `network_monitor`: View peer connections and network stats
- `reward_distributor`: Manage asset reward distributions

Run any example:
```bash
python examples/<example_name>/main.py
```

## Development

```bash
# Clone the repository
git clone https://github.com/manticore-projects/evrmore-rpc.git

# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest
```

## License

MIT License - see the LICENSE file for details.

## Credits

Created by Manticore Technologies. Inspired by the original work of Hans Evrmore. 