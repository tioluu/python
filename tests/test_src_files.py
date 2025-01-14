import sys
import os
import importlib
from unittest.mock import MagicMock

# Mock the turtle module to prevent it from opening any windows
sys.modules['turtle'] = MagicMock()

def test_another_module_import():
    try:
        # Add 'src' to the Python path to allow imports
        sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
        
        # Try importing 'another_module' to see if there are any import errors
        import another_module
    except Exception as e:
        assert False, f"Error in another_module.py: {e}"

def test_coffee_machine_execution():
    try:
        # Add 'src' to the Python path to allow imports
        sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
        
        # Try importing 'Coffee_machine_d16' to see if there are any import errors
        import Coffee_machine_d16
    except Exception as e:
        assert False, f"Error in Coffee_machine_d16.py: {e}"
