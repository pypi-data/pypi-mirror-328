"""RPC method descriptors"""
from typing import Optional, Type, TypeVar, Any, Union, get_origin, get_args
from pydantic import BaseModel
from evrmore_rpc.models.base import RPCRequest

T = TypeVar('T')

class RPCMethod:
    """Descriptor class for RPC methods"""
    def __init__(self, method_name: str, request_model: Optional[Type[RPCRequest]] = None, response_model: Optional[Union[Type[BaseModel], Type[T]]] = None):
        self.method_name = method_name
        self.request_model = request_model
        self.response_model = response_model
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        
        def caller(*args, **kwargs) -> Any:
            # If we have a request model, validate the request
            if self.request_model:
                try:
                    # Create request model instance
                    if args and not kwargs:
                        # Check if model has custom __init__
                        if hasattr(self.request_model, '__init__') and self.request_model.__init__ != BaseModel.__init__:
                            # Use positional args with custom __init__
                            model = self.request_model(*args)
                        else:
                            # Use default handling for models without custom __init__
                            model = self.request_model(
                                method=self.method_name,
                                params=list(args),
                                id=obj._get_request_id()
                            )
                    else:
                        # If kwargs provided, use request model's constructor
                        if 'method' not in kwargs:
                            kwargs['method'] = self.method_name
                        if 'id' not in kwargs:
                            kwargs['id'] = obj._get_request_id()
                        model = self.request_model(**kwargs)
                except Exception as e:
                    raise ValueError(f"Invalid parameters for {self.method_name}: {str(e)}")
                
                # Use model's params for the RPC call if they exist
                validated_args = model.params if hasattr(model, 'params') else []
            else:
                validated_args = args
            
            # Make the RPC call
            result = obj._call_method(self.method_name, *validated_args)
            
            # Special cases for non-verbose modes
            if self.method_name == 'getblock' and validated_args and len(validated_args) > 1 and validated_args[1] == 0:
                return result
            if self.method_name == 'getblockheader' and validated_args and len(validated_args) > 1 and validated_args[1] is False:
                return result
            
            # If we have a response model and it's a Pydantic model, validate the response
            if self.response_model and result is not None:
                # Handle subscripted generics (e.g., List[str], Dict[str, Any])
                origin = get_origin(self.response_model)
                if origin is not None:
                    # For container types like List, Dict, etc.
                    args = get_args(self.response_model)
                    if origin is list:
                        if len(args) > 0 and isinstance(args[0], type):
                            if issubclass(args[0], BaseModel):
                                return [args[0].model_validate(x) for x in result]
                            else:
                                return [args[0](x) if not isinstance(x, args[0]) else x for x in result]
                        return result
                    elif origin is dict:
                        if len(args) > 1 and isinstance(args[1], type):
                            if issubclass(args[1], BaseModel):
                                return {k: args[1].model_validate(v) for k, v in result.items()}
                            else:
                                return {k: args[1](v) if not isinstance(v, args[1]) else v for k, v in result.items()}
                        return result
                    return result
                elif isinstance(self.response_model, type):
                    if issubclass(self.response_model, BaseModel):
                        return self.response_model.model_validate(result)
                    elif not isinstance(result, self.response_model):
                        return self.response_model(result)
            
            return result
        
        return caller

__all__ = ['RPCMethod'] 