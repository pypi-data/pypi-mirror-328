"""Utility functions for schema analysis."""
from typing import Dict, Any
import hashlib
import json


def generate_schema_hash(schema_info: Dict[str, Any]) -> str:
    """Generate hash for schema.
    
    Args:
        schema_info: Schema information
        
    Returns:
        Schema hash string
    """
    # Sort schema info for consistent hashing
    sorted_info = _sort_dict_recursively(schema_info)
    
    # Convert to string and hash
    schema_str = json.dumps(sorted_info, sort_keys=True)
    return hashlib.sha256(schema_str.encode()).hexdigest()


def _sort_dict_recursively(obj: Any) -> Any:
    """Sort dictionary recursively.
    
    Args:
        obj: Object to sort
        
    Returns:
        Sorted object
    """
    if isinstance(obj, dict):
        return {
            k: _sort_dict_recursively(v)
            for k, v in sorted(obj.items())
        }
    elif isinstance(obj, list):
        return sorted(
            _sort_dict_recursively(x) for x in obj
        )
    else:
        return obj
