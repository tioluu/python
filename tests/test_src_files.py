import sys
import os
import importlib
from unittest.mock import MagicMock

# Mock the turtle module to prevent it from opening any windows
sys.modules['turtle'] = MagicMock()

def test_coffee_maker_execution():
    try:
        # Add 'src' to the Python path to allow imports
        sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
        
        # Try importing 'coffee_maker' to see if there are any import errors
        import coffee_maker
    except Exception as e:
        assert False, f"Error in coffee_machine_d16.py: {e}"
