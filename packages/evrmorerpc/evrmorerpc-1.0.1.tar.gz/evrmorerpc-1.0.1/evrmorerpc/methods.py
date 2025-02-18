"""RPC method descriptors"""
from typing import Optional, Type, TypeVar, Any
from evrmorerpc.models.base import RPCRequest

T = TypeVar('T')

class RPCMethod:
    """Descriptor class for RPC methods"""
    def __init__(self, method_name: str, request_model: Optional[Type[RPCRequest]] = None, response_model: Optional[Type[T]] = None):
        self.method_name = method_name
        self.request_model = request_model
        self.response_model = response_model
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        
        def caller(*args, **kwargs) -> Any:
            # If we have a request model, validate the request
            if self.request_model:
                request = self.request_model(
                    method=self.method_name,
                    params=list(args),
                    id=obj._get_request_id()
                )
                validated_args = request.params
            else:
                validated_args = args
            
            # Make the RPC call
            result = obj._call_method(self.method_name, *validated_args)
            
            # If we have a response model, validate the response
            if self.response_model and result is not None:
                return self.response_model.parse_obj(result)
            
            return result
        
        return caller

__all__ = ['RPCMethod'] 