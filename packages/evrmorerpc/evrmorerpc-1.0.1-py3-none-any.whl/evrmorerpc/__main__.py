"""Command line interface for testing RPC functionality

This module provides a command-line interface for testing various RPC commands
and functionality. It can be run directly with:

    python -m evrmorerpc <command> [args...]

Examples:
    python -m evrmorerpc getblockcount
    python -m evrmorerpc getblock <blockhash>
    python -m evrmorerpc getassetdata CREDITS
"""
import sys
import time
from typing import Optional, List, Dict, Any
from decimal import Decimal

from evrmorerpc import (
    EvrmoreRPC,
    RPCError, NodeConnectionError, NodeAuthError, EvrmoreError
)

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

def print_help() -> None:
    """Print usage help"""
    print("Usage: python -m evrmorerpc <command> [args...]")
    print("\nAvailable commands:")
    
    print("\n  Blockchain:")
    print("    getbestblockhash")
    print("    getblock <hash>")
    print("    getblockchaininfo")
    print("    getblockcount")
    print("    getblockhash <height>")
    print("    getblockheader <hash>")
    print("    getchaintips")
    print("    getdifficulty")
    print("    getmempoolinfo")
    print("    getrawmempool [verbose=false]")
    print("    gettxout <txid> <n> [include_mempool=true]")
    print("    gettxoutsetinfo")
    print("    verifychain [checklevel=3] [nblocks=6]")
    
    print("\n  Assets:")
    print("    getassetdata <asset_name>")
    print("    getcacheinfo")
    print("    getsnapshot <asset_name> <block_height>")
    print("    listaddressesbyasset <asset_name>")
    print("    listassetbalancesbyaddress <address>")
    print("    listassets [asset] [verbose=false] [count=50000] [start=0]")
    print("    listmyassets [asset] [verbose=false] [count=50000] [start=0]")
    
    print("\n  Wallet:")
    print("    abandontransaction <txid>")
    print("    addmultisigaddress <nrequired> <keys> [label]")
    print("    addwitnessaddress <address>")
    print("    dumpprivkey <address>")
    print("    getbalance [dummy=*] [minconf=1] [include_watchonly=false]")
    print("    getnewaddress [label] [address_type]")
    print("    getrawchangeaddress")
    print("    gettransaction <txid> [include_watchonly=false]")
    print("    getunconfirmedbalance")
    print("    getwalletinfo")
    print("    importaddress <address> [label] [rescan=true]")
    print("    importprivkey <privkey> [label] [rescan=true]")
    print("    importprunedfunds <rawtransaction> <txoutproof>")
    print("    importpubkey <pubkey> [label] [rescan=true]")
    print("    keypoolrefill [newsize=100]")
    print("    listaccounts [minconf=1] [include_watchonly=false]")
    print("    listaddressgroupings")
    print("    listlockunspent")
    print("    listreceivedbyaddress [minconf=1] [include_empty=false] [include_watchonly=false]")
    print("    listsinceblock [blockhash] [target_confirmations] [include_watchonly=false]")
    print("    listtransactions [label] [count=10] [skip=0] [include_watchonly=false]")
    print("    listunspent [minconf=1] [maxconf=9999999] [addresses=[] [include_unsafe=true]]")
    print("    lockunspent <unlock> <transactions>")
    print("    settxfee <amount>")
    print("    signmessage <address> <message>")
    
    print("\n  Network:")
    print("    addnode <node> <command>")
    print("    clearbanned")
    print("    disconnectnode [address] [nodeid]")
    print("    getaddednodeinfo [node]")
    print("    getconnectioncount")
    print("    getnettotals")
    print("    getnetworkinfo")
    print("    getpeerinfo")
    print("    listbanned")
    print("    ping")
    print("    setban <subnet> <command> [bantime=0] [absolute=false]")
    print("    setnetworkactive <state>")
    
    print("\n  Mining:")
    print("    getmininginfo")
    print("    getnetworkhashps [nblocks=120] [height=-1]")
    print("    prioritisetransaction <txid> <priority_delta> <fee_delta>")
    print("    submitblock <hexdata> [dummy]")
    
    print("\n  Raw Transactions:")
    print("    createrawtransaction <inputs> <outputs> [locktime=0]")
    print("    decoderawtransaction <hexstring>")
    print("    decodescript <hexstring>")
    print("    fundrawtransaction <hexstring>")
    print("    getrawtransaction <txid> [verbose=false]")
    print("    sendrawtransaction <hexstring>")
    print("    signrawtransaction <hexstring> [prevtxs=[] [privkeys=[] [sighashtype=ALL]]]")
    
    print("\n  Control:")
    print("    getmemoryinfo [mode=stats]")
    print("    getrpcinfo")
    print("    help [command]")
    print("    uptime")
    
    print("\n  Utility:")
    print("    createmultisig <nrequired> <keys>")
    print("    estimatefee [nblocks]")
    print("    validateaddress <address>")
    print("    verifymessage <address> <signature> <message>")
    
    print("\nSkipped commands (require funds or special handling):")
    for cmd, reason in SKIP_COMMANDS.items():
        print(f"    {cmd}: {reason}")
    
    print("\nFor more information about a specific command:")
    print("  python -m evrmorerpc help <command>")

def main() -> None:
    """Main function"""
    if len(sys.argv) < 2 or sys.argv[1] in ['-h', '--help', 'help']:
        print_help()
        sys.exit(0)
    
    command = sys.argv[1]
    args = sys.argv[2:]
    
    # Check if command should be skipped
    if command in SKIP_COMMANDS:
        print(f"\nSkipping command '{command}':")
        print(f"  {SKIP_COMMANDS[command]}")
        sys.exit(0)
    
    client = EvrmoreRPC()
    
    try:
        # Get the method from the client
        method = getattr(client, command, None)
        if method is None:
            print(f"Error: Unknown command '{command}'")
            print("Use 'python -m evrmorerpc help' to see available commands")
            sys.exit(1)
        
        # Execute the command with any provided arguments
        result = method(*args)
        
        # Pretty print the result
        if hasattr(result, '__dict__'):
            # For model objects, print their fields
            for field, value in result.__dict__.items():
                print(f"{field}: {value}")
        else:
            # For simple types, just print the value
            print(result)
            
    except NodeConnectionError as e:
        print("\nFailed to connect to Evrmore node:")
        print(f"  {str(e)}")
        sys.exit(1)
        
    except NodeAuthError as e:
        print("\nAuthentication failed:")
        print(f"  {str(e)}")
        print("\nPlease check your rpcuser and rpcpassword settings in evrmore.conf")
        sys.exit(1)
        
    except EvrmoreError as e:
        print(f"\nEvrmore Error [{e.code}] in {e.method}:")
        print(f"  {str(e)}")
        sys.exit(1)
        
    except Exception as e:
        print(f"\nUnexpected error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
