"""Command line interface for Evrmore RPC functionality

This module provides a command-line interface for interacting with an Evrmore node.
It can be run directly with:

    evrmore_rpc <command> [args...]

Examples:
    evrmore_rpc getblockcount
    evrmore_rpc getblock <blockhash>
    evrmore_rpc getassetdata CREDITS
"""
import sys
import time
from typing import Optional, List, Dict, Any, Tuple
from decimal import Decimal
from pathlib import Path

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.syntax import Syntax
from rich.live import Live
from rich.layout import Layout
from rich.align import Align
from rich.prompt import Prompt
from rich import box
from rich.columns import Columns
from rich.padding import Padding

from prompt_toolkit import Application
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.layout.layout import Layout as PTLayout
from prompt_toolkit.layout.dimension import Dimension
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.keys import Keys
from prompt_toolkit.styles import Style
from prompt_toolkit.formatted_text import HTML

from evrmore_rpc import (
    evrmore_rpc,
    RPCError, NodeConnectionError, NodeAuthError, EvrmoreError
)

# Initialize rich console
console = Console()

# Commands that cost money or require special handling
SKIP_COMMANDS = {
    'issue': "Skipped: Costs EVR to issue assets",
    'issueunique': "Skipped: Costs EVR to issue unique assets",
    'reissue': "Skipped: Costs EVR to reissue assets",
    'backupwallet': "Skipped: Requires filesystem access",
    'dumpwallet': "Skipped: Requires filesystem access",
    'importwallet': "Skipped: Requires filesystem access",
    'encryptwallet': "Skipped: Would lock the wallet",
    'walletpassphrase': "Skipped: Requires encrypted wallet",
    'walletpassphrasechange': "Skipped: Requires encrypted wallet",
    'stop': "Skipped: Would stop the node",
}

# Command categories with colors and icons
COMMAND_CATEGORIES = {
    'Blockchain': {
        'color': 'blue',
        'icon': '🔗',
        'commands': [
            ('getbestblockhash', 'Get the hash of the best (tip) block in the longest blockchain'),
            ('getblock', '<hash> [verbosity=1] Get block information'),
            ('getblockchaininfo', 'Get current blockchain information'),
            ('getblockcount', 'Get the current block height'),
            ('getblockhash', '<height> Get block hash at height'),
            ('getblockheader', '<hash> [verbose=true] Get block header information'),
            ('getchaintips', 'Get information about all known chain tips'),
            ('getdifficulty', 'Get proof-of-work difficulty'),
            ('getmempoolinfo', 'Get transaction memory pool information'),
            ('getrawmempool', '[verbose=false] Get all transaction IDs in memory pool'),
            ('gettxout', '<txid> <n> [include_mempool=true] Get unspent transaction output'),
            ('gettxoutsetinfo', 'Get statistics about the unspent transaction output set'),
            ('verifychain', '[checklevel=3] [nblocks=6] Verify blockchain database'),
        ]
    },
    'Assets': {
        'color': 'green',
        'icon': '💎',
        'commands': [
            ('getassetdata', '<asset_name> Get asset metadata'),
            ('getcacheinfo', 'Get asset cache statistics'),
            ('getsnapshot', '<asset_name> <block_height> Get snapshot of asset holders'),
            ('listaddressesbyasset', '<asset_name> List addresses holding an asset'),
            ('listassetbalancesbyaddress', '<address> List asset balances for address'),
            ('listassets', '[asset] [verbose=false] [count=50000] [start=0] List assets'),
            ('listmyassets', '[asset] [verbose=false] [count=50000] [start=0] List my assets'),
        ]
    },
    'Wallet': {
        'color': 'yellow',
        'icon': '👛',
        'commands': [
            ('abandontransaction', '<txid> Mark transaction for abandonment'),
            ('addmultisigaddress', '<nrequired> <keys> [label] Add multisig address'),
            ('addwitnessaddress', '<address> Add witness address'),
            ('dumpprivkey', '<address> Reveal private key for address'),
            ('getbalance', '[dummy=*] [minconf=1] [include_watchonly=false] Get wallet balance'),
            ('getnewaddress', '[label] [address_type] Generate new address'),
            ('getrawchangeaddress', 'Generate new change address'),
            ('gettransaction', '<txid> [include_watchonly=false] Get transaction details'),
            ('getunconfirmedbalance', 'Get unconfirmed balance'),
            ('getwalletinfo', 'Get wallet state information'),
            ('importaddress', '<address> [label] [rescan=true] Import address'),
            ('importprivkey', '<privkey> [label] [rescan=true] Import private key'),
            ('importprunedfunds', '<rawtransaction> <txoutproof> Import pruned funds'),
            ('importpubkey', '<pubkey> [label] [rescan=true] Import public key'),
            ('keypoolrefill', '[newsize=100] Fill key pool'),
            ('listaccounts', '[minconf=1] [include_watchonly=false] DEPRECATED List accounts'),
            ('listaddressgroupings', 'List address groupings'),
            ('listlockunspent', 'List unspent outputs marked as unspendable'),
            ('listreceivedbyaddress', '[minconf=1] [include_empty=false] [include_watchonly=false] List balances by address'),
            ('listsinceblock', '[blockhash] [target_confirmations] [include_watchonly=false] Get all transactions since block'),
            ('listtransactions', '[label] [count=10] [skip=0] [include_watchonly=false] List transactions'),
            ('listunspent', '[minconf=1] [maxconf=9999999] [addresses=[] [include_unsafe=true]] List unspent outputs'),
            ('lockunspent', '<unlock> <transactions> Lock/unlock unspent outputs'),
            ('settxfee', '<amount> Set transaction fee per kB'),
            ('signmessage', '<address> <message> Sign a message with address key'),
        ]
    },
    'Network': {
        'color': 'cyan',
        'icon': '🌐',
        'commands': [
            ('addnode', '<node> <command> Add/remove/onetry a node'),
            ('clearbanned', 'Clear list of banned nodes'),
            ('disconnectnode', '[address] [nodeid] Disconnect node'),
            ('getaddednodeinfo', '[node] Get information about added nodes'),
            ('getconnectioncount', 'Get number of connections'),
            ('getnettotals', 'Get network traffic statistics'),
            ('getnetworkinfo', 'Get network information'),
            ('getpeerinfo', 'Get peer connection information'),
            ('listbanned', 'List banned hosts'),
            ('ping', 'Request that nodes ping us'),
            ('setban', '<subnet> <command> [bantime=0] [absolute=false] Ban a host'),
            ('setnetworkactive', '<state> Enable/disable networking'),
        ]
    },
    'Mining': {
        'color': 'magenta',
        'icon': '⛏️',
        'commands': [
            ('getmininginfo', 'Get mining-related information'),
            ('getnetworkhashps', '[nblocks=120] [height=-1] Get network hashes per second'),
            ('prioritisetransaction', '<txid> <priority_delta> <fee_delta> Change transaction priority'),
            ('submitblock', '<hexdata> [dummy] Submit new block'),
        ]
    },
    'Raw Transactions': {
        'color': 'red',
        'icon': '📝',
        'commands': [
            ('createrawtransaction', '<inputs> <outputs> [locktime=0] Create raw transaction'),
            ('decoderawtransaction', '<hexstring> Decode raw transaction'),
            ('decodescript', '<hexstring> Decode a hex-encoded script'),
            ('fundrawtransaction', '<hexstring> Add inputs to raw transaction'),
            ('getrawtransaction', '<txid> [verbose=false] Get raw transaction'),
            ('sendrawtransaction', '<hexstring> Submit raw transaction'),
            ('signrawtransaction', '<hexstring> [prevtxs=[] [privkeys=[] [sighashtype=ALL]]] Sign raw transaction'),
        ]
    },
    'Control': {
        'color': 'bright_blue',
        'icon': '🎮',
        'commands': [
            ('getmemoryinfo', '[mode=stats] Get memory usage information'),
            ('getrpcinfo', 'Get RPC server information'),
            ('help', '[command] Get help for a command'),
            ('uptime', 'Get node uptime'),
        ]
    },
    'Utility': {
        'color': 'bright_green',
        'icon': '🔧',
        'commands': [
            ('createmultisig', '<nrequired> <keys> Create multisig address'),
            ('estimatefee', '[nblocks] Estimate fee rate'),
            ('validateaddress', '<address> Verify an address is valid'),
            ('verifymessage', '<address> <signature> <message> Verify a signed message'),
        ]
    }
}

def create_category_panel(category: str, data: Dict) -> Panel:
    """Create a rich panel for a command category"""
    # Create a table for commands
    table = Table(
        show_header=False,
        box=None,
        padding=(0, 1),
        collapse_padding=True
    )
    table.add_column(style=f"{data['color']}")
    
    # Add commands to table
    for cmd, desc in data['commands']:
        table.add_row(f"[bold]{cmd}[/]")
    
    return Panel(
        table,
        title=f"{data['icon']} {category}",
        title_align="left",
        border_style=data['color'],
        box=box.ROUNDED
    )

def show_command_details(category: str, command: str, desc: str, color: str, icon: str) -> Panel:
    """Show detailed information about a command"""
    example = get_command_example(command)
    content = Text.from_markup(
        f"\n[bold]{command}[/]\n\n"
        f"{desc}\n\n"
        f"[bold]Usage:[/]\n"
        f"  evrmore_rpc {command} {example}\n"
    )
    
    return Panel(
        content,
        title=f"{icon} Command Details",
        border_style=color,
        box=box.ROUNDED,
        padding=(1, 2)
    )

class HelpApp:
    def __init__(self):
        self.categories = list(COMMAND_CATEGORIES.keys())
        self.current_category = 0
        self.current_command = 0
        self.in_category = False
        self.in_command_details = False
        self.selected_category = None
        
        # Create key bindings
        self.kb = KeyBindings()
        
        @self.kb.add('q')
        def _(event):
            event.app.exit()
            
        @self.kb.add('up')
        def _(event):
            w = event.app.layout.current_window
            if self.in_category:
                self.current_command = max(0, self.current_command - 1)
                # Ensure selected command is visible
                if self.current_command < w.vertical_scroll:
                    w.vertical_scroll = self.current_command
            else:
                self.current_category = max(0, self.current_category - 1)
                # Ensure selected category is visible
                if self.current_category < w.vertical_scroll:
                    w.vertical_scroll = self.current_category
            self._refresh_screen()
            
        @self.kb.add('down')
        def _(event):
            w = event.app.layout.current_window
            if self.in_category:
                commands = COMMAND_CATEGORIES[self.selected_category]['commands']
                self.current_command = min(len(commands) - 1, self.current_command + 1)
                # Ensure selected command is visible
                visible_lines = w.render_info.window_height - 4  # Account for header/footer
                if self.current_command > w.vertical_scroll + visible_lines:
                    w.vertical_scroll = max(0, self.current_command - visible_lines + 1)
            else:
                self.current_category = min(len(self.categories) - 1, self.current_category + 1)
                # Ensure selected category is visible
                visible_lines = w.render_info.window_height - 4  # Account for header/footer
                if self.current_category > w.vertical_scroll + visible_lines:
                    w.vertical_scroll = max(0, self.current_category - visible_lines + 1)
            self._refresh_screen()
            
        @self.kb.add('left')
        def _(event):
            if self.in_command_details:
                self.in_command_details = False
                self._refresh_screen()
            elif self.in_category:
                self.in_category = False
                self.current_command = 0
                self._refresh_screen()
                
        @self.kb.add('right')
        def _(event):
            self._handle_selection(event)
            
        @self.kb.add(Keys.Enter)
        def _(event):
            self._handle_selection(event)

        @self.kb.add('pageup')
        def _(event):
            w = event.app.layout.current_window
            w.vertical_scroll = max(0, w.vertical_scroll - w.render_info.window_height)

        @self.kb.add('pagedown')
        def _(event):
            w = event.app.layout.current_window
            w.vertical_scroll = min(w.vertical_scroll + w.render_info.window_height, w.render_info.content_height)
                
        # Create the layout with scrolling support
        self.main_container = HSplit([
            Window(FormattedTextControl(self._get_header), height=3),
            Window(
                FormattedTextControl(self._get_content),
                wrap_lines=True,
                always_hide_cursor=True,
                allow_scroll_beyond_bottom=True,
            ),
            Window(FormattedTextControl(self._get_footer), height=2),
        ])
        
        # Create the application
        self.app = Application(
            layout=PTLayout(self.main_container),
            key_bindings=self.kb,
            full_screen=True,
            style=Style.from_dict({
                'category': 'bold',
                'selected': 'reverse',
                'command': '',
                'description': '#AAAAAA',
                'header': 'bold',
                'footer': '#666666',
            }),
            mouse_support=True
        )
    
    def _get_header(self) -> List[Tuple[str, str]]:
        """Get the header content"""
        return [
            ('class:header', '\n  Evrmore RPC Command Line Interface\n\n')
        ]
    
    def _get_footer(self) -> List[Tuple[str, str]]:
        """Get the footer content"""
        if self.in_command_details:
            return [('class:footer', '  ← Back | PgUp/PgDn Scroll | q Quit')]
        elif self.in_category:
            return [('class:footer', '  ← Back | → Details | ↑↓ Navigate | PgUp/PgDn Scroll | q Quit')]
        else:
            return [('class:footer', '  →/Enter Select | ↑↓ Navigate | PgUp/PgDn Scroll | q Quit')]
    
    def _get_content(self) -> List[Tuple[str, str]]:
        """Get the main content"""
        if self.in_command_details:
            return self._get_command_details()
        elif self.in_category:
            return self._get_category_commands()
        else:
            return self._get_categories()
    
    def _get_categories(self) -> List[Tuple[str, str]]:
        """Get the category list"""
        result = []
        for i, category in enumerate(self.categories):
            data = COMMAND_CATEGORIES[category]
            prefix = '  → ' if i == self.current_category else '    '
            style = 'class:selected' if i == self.current_category else 'class:category'
            result.extend([
                ('', prefix),
                (style, f"{data['icon']} {category}"),
                ('', '\n')
            ])
        return result
    
    def _get_category_commands(self) -> List[Tuple[str, str]]:
        """Get the command list for current category"""
        result = []
        data = COMMAND_CATEGORIES[self.selected_category]
        result.extend([
            ('class:header', f"\n  {data['icon']} {self.selected_category}\n\n")
        ])
        
        for i, (cmd, desc) in enumerate(data['commands']):
            prefix = '  → ' if i == self.current_command else '    '
            cmd_style = 'class:selected' if i == self.current_command else 'class:command'
            result.extend([
                ('', prefix),
                (cmd_style, cmd),
                ('class:description', f" - {desc}"),
                ('', '\n')
            ])
        return result
    
    def _get_command_details(self) -> List[Tuple[str, str]]:
        """Get detailed view of current command"""
        data = COMMAND_CATEGORIES[self.selected_category]
        cmd, desc = data['commands'][self.current_command]
        example = get_command_example(cmd)
        
        return [
            ('class:header', f"\n  {data['icon']} {cmd}\n\n"),
            ('class:description', f"  {desc}\n\n"),
            ('class:command', "  Usage:\n"),
            ('', f"    evrmore_rpc {cmd} {example}\n")
        ]
    
    def _refresh_screen(self) -> None:
        """Force screen refresh"""
        self.app.invalidate()
    
    def _handle_selection(self, event):
        """Handle selection via Enter or Right arrow"""
        if not self.in_category:
            self.in_category = True
            self.selected_category = self.categories[self.current_category]
            self._refresh_screen()
        elif not self.in_command_details:
            self.in_command_details = True
            self._refresh_screen()
    
    def run(self) -> None:
        """Run the application"""
        self.app.run()

def show_interactive_help() -> None:
    """Show interactive help with animations"""
    app = HelpApp()
    app.run()

def get_command_example(command: str) -> str:
    """Get example usage for a command"""
    examples = {
        'getblock': '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f',
        'getblockhash': '1',
        'getassetdata': 'CREDITS',
        'getnewaddress': 'mylabel legacy',
        'sendtoaddress': 'EXaMPLEaDDreSS123456789 1.0',
        'validateaddress': 'EXaMPLEaDDreSS123456789',
    }
    return examples.get(command, '')

def format_result(result: Any) -> None:
    """Format and print command result with rich formatting"""
    if hasattr(result, '__dict__'):
        # For model objects, create a table
        table = Table(show_header=True, header_style="bold blue", box=box.ROUNDED)
        table.add_column("Field", style="cyan")
        table.add_column("Value", style="green")
        
        for field, value in result.__dict__.items():
            if not field.startswith('_'):
                table.add_row(field, str(value))
        
        console.print(table)
    else:
        # For simple types, print with appropriate formatting
        if isinstance(result, (dict, list)):
            console.print_json(data=result)
        elif isinstance(result, str) and len(result) > 64:
            # Likely a hash or hex string
            console.print(Syntax(result, "hex", theme="monokai"))
        else:
            console.print(str(result), style="green")

def main() -> None:
    """Main entry point for CLI"""
    if len(sys.argv) < 2 or sys.argv[1] in ['-h', '--help', 'help'] and len(sys.argv) == 2:
        show_interactive_help()
        sys.exit(0)
    
    command = sys.argv[1]
    args = sys.argv[2:]
    
    # Check if command should be skipped
    if command in SKIP_COMMANDS:
        console.print(f"\n[red]Skipping command '{command}':")
        console.print(f"  {SKIP_COMMANDS[command]}[/]")
        sys.exit(0)
    
    try:
        with console.status("[bold blue]Connecting to Evrmore node...") as status:
            client = evrmore_rpc()
            status.update("[bold blue]Connected! Executing command...")
        
        # Get the method from the client
        method = getattr(client, command, None)
        if method is None:
            console.print(f"[red]Error: Unknown command '{command}'")
            console.print("[yellow]Use 'evrmore_rpc help' to see available commands[/]")
            sys.exit(1)
        
        # Execute the command with any provided arguments
        result = method(*args)
        format_result(result)
        
    except NodeConnectionError as e:
        console.print("\n[red]Failed to connect to Evrmore node:")
        console.print(f"  {str(e)}")
        console.print("\n[yellow]Please ensure:")
        console.print("  1. The Evrmore daemon (evrmored) is running")
        console.print("  2. Your evrmore.conf is properly configured")
        console.print("  3. The RPC port (default: 8819) is accessible[/]")
        sys.exit(1)
        
    except NodeAuthError as e:
        console.print("\n[red]Authentication failed:")
        console.print(f"  {str(e)}")
        console.print("\n[yellow]Please check your rpcuser and rpcpassword settings in evrmore.conf[/]")
        sys.exit(1)
        
    except EvrmoreError as e:
        console.print(f"\n[red]Evrmore Error [{e.code}] in {e.method}:")
        console.print(f"  {str(e)}[/]")
        sys.exit(1)
        
    except Exception as e:
        console.print(f"\n[red]Unexpected error: {str(e)}[/]")
        sys.exit(1)

if __name__ == "__main__":
    main()
