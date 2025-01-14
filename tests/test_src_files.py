import sys
from unittest.mock import MagicMock

# Mock the turtle module to prevent it from opening any windows
sys.modules['turtle'] = MagicMock()

import importlib
import os
import sys

def test_another_module_import():
    try:
        # Add 'src' to the Python path to allow imports
        sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
        
        # Check if there are any errors when executing the file
        file_path = os.path.join("src", "another_module.py")
        with open(file_path) as f:
            exec(f.read())
    except Exception as e:
        assert False, f"Error in another_module.py: {e}"

def test_coffee_machine_execution():
    try:
        # Add 'src' to the Python path to allow imports
        sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
        
        # Execute Coffee_machine_d16.py as a script
        file_path = os.path.join("src", "Coffee_machine_d16.py")
        with open(file_path) as f:
            exec(f.read())
    except Exception as e:
        assert False, f"Error in Coffee_machine_d16.py: {e}"