# ACS_retriever/__init__.py

import importlib
import inspect

# List the module names (without the .py extension)
modules = ['DP02_functions', 'DP03_functions', 
           'DP04_functions', 'DP05_functions']

__all__ = []

for module_name in modules:
    
    # Import the module using relative import (e.g., from .DP02_functions import ...)
    module = importlib.import_module(f'.{module_name}', package=__name__)
    
    # Get all functions defined *in that module* using inspect
    # This filters out imported helper functions that may not belong in the public API
    functions = {
        name: func for name, func in inspect.getmembers(module, inspect.isfunction)
        if func.__module__.endswith(module_name)
    }
    
    # Add these functions to the current module's namespace
    globals().update(functions)
    
    # Add their names to __all__ so they're part of the public API
    __all__.extend(functions.keys())
