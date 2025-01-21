import pytest
import sys
import os
from unittest.mock import patch

# Fixture to set up and clean up sys.path
@pytest.fixture(scope="function", autouse=True)
def add_src_to_path():
    # Add 'src' to the Python path to allow imports from that directory
    original_sys_path = sys.path[:]
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
    yield
    # Clean up by restoring sys.path after the test
    sys.path = original_sys_path

def test_coffee_maker_execution():
    try:
        # Try importing 'coffee_maker' to see if there are any import errors
        import coffee_maker
    except Exception as e:
        assert False, f"Error in coffee_maker.py: {e}"

def test_main_execution():
    # Mock inputs for the program
    inputs = ['espresso', 'off']  # Simulated user inputs
    with patch('builtins.input', side_effect=inputs):
        try:
            # Try importing 'main' to see if there are any import errors
            import main
        except Exception as e:
            assert False, f"Error in main.py: {e}"

def test_menu_execution():
    try:
        # Try importing 'menu' to see if there are any import errors
        import menu
    except Exception as e:
        assert False, f"Error in menu.py: {e}"

def test_money_machine():
    try:
        # Try importing 'money_machine' to see if there are any import errors
        import money_machine
    except Exception as e:
        assert False, f"Error in money_machine.py: {e}"
