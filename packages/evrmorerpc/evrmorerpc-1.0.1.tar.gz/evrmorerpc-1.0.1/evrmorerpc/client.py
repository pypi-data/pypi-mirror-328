"""Evrmore RPC client implementation"""
import requests
from typing import Any, Dict, Optional
from decimal import Decimal
from pathlib import Path

from evrmorerpc.errors import NodeConnectionError, NodeAuthError, EvrmoreError
from evrmorerpc.methods import RPCMethod
from evrmorerpc.config import load_config, EvrmoreConfigError
from evrmorerpc.models.base import RPCRequest, RPCResponse
from evrmorerpc.models.blockchain import (
    BlockInfoResponse,
    GetBlockRequest,
    GetBlockHashRequest,
    BlockHeaderResponse,
    MempoolInfoResponse
)
from evrmorerpc.models.assets import (
    AssetInfoResponse,
    GetAssetDataRequest,
    IssueAssetRequest,
    TransferAssetRequest
)
from evrmorerpc.models.network import NetworkInfoResponse
from evrmorerpc.models.wallet import (
    WalletInfoResponse,
    TransactionInfoResponse,
    GetTransactionRequest
)
from evrmorerpc.models.mining import MiningInfoResponse
from evrmorerpc.models.control import MemoryInfoResponse, RPCInfoResponse

class EvrmoreRPC:
    """Evrmore RPC client"""
    
    def __init__(self, config_path: Optional[Path] = None):
        """Initialize RPC client
        
        Args:
            config_path: Optional path to evrmore.conf. If not provided,
                        will look in default location (~/.evrmore/evrmore.conf)
                        or use EVRMORE_ROOT environment variable.
        
        Raises:
            EvrmoreConfigError: If configuration is invalid or cannot be loaded
        """
        # Load and validate configuration
        config = load_config(config_path)
        
        self.rpc_user = config['rpcuser']
        self.rpc_password = config['rpcpassword']
        self.rpc_port = config['rpcport']
        self.rpc_host = config.get('rpcbind', '127.0.0.1')
        
        # Build RPC URL
        self.url = f"http://{self.rpc_host}:{self.rpc_port}"
        
        # Initialize session with auth
        self.session = requests.Session()
        self.session.auth = (self.rpc_user, self.rpc_password)
        self.session.headers['content-type'] = 'application/json'
        
        # Request ID counter
        self._request_id = 0
    
    def _get_request_id(self) -> int:
        """Get unique request ID"""
        self._request_id += 1
        return self._request_id
    
    def _call_method(self, method: str, *args) -> Any:
        """Make RPC call to Evrmore node
        
        Args:
            method: RPC method name
            *args: Method arguments
            
        Returns:
            Response from node
            
        Raises:
            NodeConnectionError: Connection to node failed
            NodeAuthError: Authentication failed
            EvrmoreError: Node returned an Evrmore-specific error
        """
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": args,
            "id": self._get_request_id()
        }
        
        # Some commands need longer timeouts
        timeout = 30 if method in ['gettxoutsetinfo'] else 10
        
        try:
            response = self.session.post(self.url, json=payload, timeout=timeout)
            
            # Check for auth error
            if response.status_code == 401:
                raise NodeAuthError("Authentication failed - check rpcuser/rpcpassword")
            
            # Try to parse response even if status code is error
            result = response.json()
            
            # Validate response structure
            response_model = RPCResponse.parse_obj(result)
            
            # Check for RPC error
            if response_model.error is not None:
                error = response_model.error
                raise EvrmoreError(
                    error.get('message', 'Unknown error'),
                    error.get('code', -1),
                    method
                )
            
            # Now check for HTTP errors after we've tried to parse potential error response
            response.raise_for_status()
                
            return response_model.result
            
        except requests.exceptions.Timeout as e:
            raise NodeConnectionError(
                f"Request timed out after {timeout} seconds"
            ) from e
        except requests.exceptions.ConnectionError as e:
            raise NodeConnectionError(
                f"Failed to connect to Evrmore node at {self.url}"
            ) from e
        except requests.exceptions.HTTPError as e:
            # If we have a parsed error response, raise EvrmoreError
            if 'result' in locals() and isinstance(result, dict) and 'error' in result and result['error']:
                error = result['error']
                raise EvrmoreError(
                    error.get('message', 'Unknown error'),
                    error.get('code', -1),
                    method
                ) from e
            raise NodeConnectionError(
                f"HTTP error occurred: {str(e)}"
            ) from e
        except requests.exceptions.RequestException as e:
            raise NodeConnectionError(
                f"Request failed: {str(e)}"
            ) from e
        except (KeyError, ValueError) as e:
            raise NodeConnectionError(
                f"Invalid response format: {str(e)}"
            ) from e
    
    # Blockchain Methods
    getbestblockhash = RPCMethod('getbestblockhash')
    getblock = RPCMethod('getblock', GetBlockRequest, BlockInfoResponse)
    getblockchaininfo = RPCMethod('getblockchaininfo')
    getblockcount = RPCMethod('getblockcount')
    getblockhash = RPCMethod('getblockhash', GetBlockHashRequest)
    getblockheader = RPCMethod('getblockheader', response_model=BlockHeaderResponse)
    getchaintips = RPCMethod('getchaintips')
    getdifficulty = RPCMethod('getdifficulty')
    getmempoolinfo = RPCMethod('getmempoolinfo', response_model=MempoolInfoResponse)
    getrawmempool = RPCMethod('getrawmempool')
    gettxout = RPCMethod('gettxout')
    gettxoutsetinfo = RPCMethod('gettxoutsetinfo')
    verifychain = RPCMethod('verifychain')
    
    # Network Methods
    getnetworkinfo = RPCMethod('getnetworkinfo', response_model=NetworkInfoResponse)
    getpeerinfo = RPCMethod('getpeerinfo')
    getconnectioncount = RPCMethod('getconnectioncount')
    ping = RPCMethod('ping')
    
    # Asset Methods
    getassetdata = RPCMethod('getassetdata', GetAssetDataRequest, AssetInfoResponse)
    getcacheinfo = RPCMethod('getcacheinfo')
    getsnapshot = RPCMethod('getsnapshot')
    issue = RPCMethod('issue', IssueAssetRequest)
    issueunique = RPCMethod('issueunique')
    listaddressesbyasset = RPCMethod('listaddressesbyasset')
    listassetbalancesbyaddress = RPCMethod('listassetbalancesbyaddress')
    listassets = RPCMethod('listassets')
    listmyassets = RPCMethod('listmyassets')
    reissue = RPCMethod('reissue')
    transfer = RPCMethod('transfer', TransferAssetRequest)
    transferfromaddress = RPCMethod('transferfromaddress')
    transferfromaddresses = RPCMethod('transferfromaddresses')
    
    # Wallet Methods
    abandontransaction = RPCMethod('abandontransaction')
    addmultisigaddress = RPCMethod('addmultisigaddress')
    addwitnessaddress = RPCMethod('addwitnessaddress')
    backupwallet = RPCMethod('backupwallet')
    dumpprivkey = RPCMethod('dumpprivkey')
    dumpwallet = RPCMethod('dumpwallet')
    encryptwallet = RPCMethod('encryptwallet')
    getbalance = RPCMethod('getbalance')
    getnewaddress = RPCMethod('getnewaddress')
    getrawchangeaddress = RPCMethod('getrawchangeaddress')
    gettransaction = RPCMethod('gettransaction', GetTransactionRequest, TransactionInfoResponse)
    getunconfirmedbalance = RPCMethod('getunconfirmedbalance')
    getwalletinfo = RPCMethod('getwalletinfo', response_model=WalletInfoResponse)
    importaddress = RPCMethod('importaddress')
    importprivkey = RPCMethod('importprivkey')
    importprunedfunds = RPCMethod('importprunedfunds')
    importpubkey = RPCMethod('importpubkey')
    importwallet = RPCMethod('importwallet')
    keypoolrefill = RPCMethod('keypoolrefill')
    listaccounts = RPCMethod('listaccounts')
    listaddressgroupings = RPCMethod('listaddressgroupings')
    listlockunspent = RPCMethod('listlockunspent')
    listreceivedbyaddress = RPCMethod('listreceivedbyaddress')
    listsinceblock = RPCMethod('listsinceblock')
    listtransactions = RPCMethod('listtransactions')
    listunspent = RPCMethod('listunspent')
    lockunspent = RPCMethod('lockunspent')
    sendmany = RPCMethod('sendmany')
    sendtoaddress = RPCMethod('sendtoaddress')
    settxfee = RPCMethod('settxfee')
    signmessage = RPCMethod('signmessage')
    walletlock = RPCMethod('walletlock')
    walletpassphrase = RPCMethod('walletpassphrase')
    walletpassphrasechange = RPCMethod('walletpassphrasechange')
    
    # Raw Transaction Methods
    createrawtransaction = RPCMethod('createrawtransaction')
    decoderawtransaction = RPCMethod('decoderawtransaction')
    decodescript = RPCMethod('decodescript')
    fundrawtransaction = RPCMethod('fundrawtransaction')
    getrawtransaction = RPCMethod('getrawtransaction')
    sendrawtransaction = RPCMethod('sendrawtransaction')
    signrawtransaction = RPCMethod('signrawtransaction')
    
    # Mining Methods
    getmininginfo = RPCMethod('getmininginfo', response_model=MiningInfoResponse)
    getnetworkhashps = RPCMethod('getnetworkhashps')
    prioritisetransaction = RPCMethod('prioritisetransaction')
    submitblock = RPCMethod('submitblock')
    
    # Control Methods
    getmemoryinfo = RPCMethod('getmemoryinfo', response_model=MemoryInfoResponse)
    getrpcinfo = RPCMethod('getrpcinfo', response_model=RPCInfoResponse)
    help = RPCMethod('help')
    stop = RPCMethod('stop')
    uptime = RPCMethod('uptime')
    
    # Utility Methods
    createmultisig = RPCMethod('createmultisig')
    estimatefee = RPCMethod('estimatefee')
    validateaddress = RPCMethod('validateaddress')
    verifymessage = RPCMethod('verifymessage')

__all__ = ['EvrmoreRPC'] 