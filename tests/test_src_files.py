from unittest.mock import patch
import pytest

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
