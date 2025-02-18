"""Error classes for RPC module"""
from typing import Optional

class RPCError(Exception):
    """Base exception for RPC errors"""
    def __init__(self, message: str, code: Optional[int] = None, method: Optional[str] = None):
        self.code = code
        self.method = method
        super().__init__(f"RPC Error [{code}] in {method}: {message}" if code else message)

class NodeConnectionError(RPCError):
    """Raised when connection to node fails"""
    pass

class NodeAuthError(RPCError):
    """Raised when authentication failed"""
    pass

class EvrmoreError(RPCError):
    """Evrmore-specific error codes and messages
    
    Common error codes:
    -1  - General error during processing
    -3  - Asset not found
    -4  - Out of memory
    -5  - Invalid parameter
    -8  - Invalid parameter combination
    -20 - Invalid address or key
    -22 - Error parsing JSON
    -25 - Error processing transaction
    -26 - Transaction already in chain
    -27 - Transaction already in mempool
    """
    # Map of known Evrmore error codes to human-readable messages
    ERROR_MESSAGES = {
        -1: "General error during processing",
        -3: "Asset not found",
        -4: "Out of memory",
        -5: "Invalid parameter",
        -8: "Invalid parameter combination",
        -20: "Invalid address or key",
        -22: "Error parsing JSON",
        -25: "Error processing transaction",
        -26: "Transaction already in chain",
        -27: "Transaction already in mempool",
    }
    
    def __init__(self, message: str, code: int, method: str):
        self.code = code
        self.method = method
        # Get standard message for known error codes
        standard_msg = self.ERROR_MESSAGES.get(code, "Unknown error")
        # Combine standard message with specific message if different
        full_msg = f"{standard_msg} - {message}" if message != standard_msg else message
        super().__init__(full_msg, code, method)

__all__ = [
    'RPCError',
    'NodeConnectionError',
    'NodeAuthError',
    'EvrmoreError'
] 