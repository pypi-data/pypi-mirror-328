"""Command line interface for testing ZMQ connections

This module provides a command-line interface for testing ZMQ connections to an Evrmore node.
It can be run directly with:
    python3 -m evrmore_rpc.zmq

The script will:
1. Connect to the Evrmore node using settings from evrmore.conf
2. Subscribe to all available ZMQ topics
3. Display incoming notifications in a human-readable format
4. Continue running until interrupted with Ctrl+C
"""
import sys
import asyncio
from pathlib import Path
from datetime import datetime

from rich.console import Console
from evrmore_rpc.config import EvrmoreConfigError
from evrmore_rpc.zmq import (
    EvrmoreZMQ, ZMQNotification, HashTxNotification, 
    RawTxNotification, HashBlockNotification, RawBlockNotification,
    SequenceNotification
)

# Initialize console
console = Console()

async def handle_notification(notification: ZMQNotification):
    """Handle ZMQ notification by displaying it in a human-readable format
    
    Args:
        notification: The ZMQ notification to display
    """
    timestamp = datetime.now().strftime("%H:%M:%S")
    
    if isinstance(notification, HashTxNotification):
        console.print(f"[{timestamp}] [bold green]New transaction:[/] {notification.txid}")
    elif isinstance(notification, RawTxNotification):
        console.print(f"[{timestamp}] [bold blue]Raw transaction:[/] {notification.size} bytes")
    elif isinstance(notification, HashBlockNotification):
        console.print(f"[{timestamp}] [bold yellow]New block:[/] {notification.blockhash}")
    elif isinstance(notification, RawBlockNotification):
        console.print(f"[{timestamp}] [bold magenta]Raw block:[/] {notification.size} bytes")
    elif isinstance(notification, SequenceNotification):
        console.print(f"[{timestamp}] [bold red]Chain reorganization[/] at height {notification.height}: {notification.blockhash}")

async def main(config_path: Path = None) -> None:
    """Main entry point for ZMQ testing
    
    Args:
        config_path: Optional path to evrmore.conf
    """
    try:
        # Create ZMQ client
        with console.status("[bold blue]Connecting to Evrmore node...") as status:
            zmq_client = EvrmoreZMQ(config_path)
            status.update("[bold blue]Connected! Subscribing to notifications...")
        
        # Subscribe to all available topics
        for topic in [b"hashtx", b"rawtx", b"hashblock", b"rawblock", b"sequence"]:
            zmq_client.subscribe([topic], handle_notification)
        
        # Print header
        console.print("\n[bold white]Evrmore ZMQ Notification Monitor[/]")
        console.print("[dim]Listening for the following notifications:[/]")
        console.print("  [bold green]• Transaction hashes[/]")
        console.print("  [bold blue]• Raw transactions[/]")
        console.print("  [bold yellow]• Block hashes[/]")
        console.print("  [bold magenta]• Raw blocks[/]")
        console.print("  [bold red]• Chain reorganizations[/]")
        console.print("\n[dim]Press Ctrl+C to stop[/]\n")
        
        # Start listening
        try:
            await zmq_client.start()
        except KeyboardInterrupt:
            console.print("\n[yellow]Stopping ZMQ client...[/]")
        finally:
            zmq_client.close()
            
    except EvrmoreConfigError as e:
        console.print(f"\n[red]Configuration error: {str(e)}[/]")
        console.print("[yellow]Make sure evrmore.conf exists and contains ZMQ settings:[/]")
        console.print("  zmqpubhashtx=tcp://127.0.0.1:28332")
        console.print("  zmqpubrawtx=tcp://127.0.0.1:28332")
        console.print("  zmqpubhashblock=tcp://127.0.0.1:28332")
        console.print("  zmqpubrawblock=tcp://127.0.0.1:28332")
        console.print("  zmqpubsequence=tcp://127.0.0.1:28332")
        sys.exit(1)
    except Exception as e:
        console.print(f"\n[red]Error: {str(e)}[/]")
        sys.exit(1)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass 