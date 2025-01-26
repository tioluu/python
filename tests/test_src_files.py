from unittest.mock import patch
import sys
import os
import importlib

def test_data():
    try:
        # Try importing 'data' to see if there are any import errors
        import data
    except Exception as e:
        assert False, f"Error in data.py: {e}"


def infinite_input_generator():
    while True:
        yield "true"  # Provide the same input repeatedly

def test_main_execution():
    # Use the generator for unlimited inputs
    input_gen = infinite_input_generator()
    
    with patch('builtins.input', side_effect=lambda: next(input_gen)), patch('sys.exit') as mock_exit:
        try:
            import main
        except SystemExit:
            pass
        except Exception as e:
            assert False, f"Error in main.py: {e}"

def test_question_model_execution():
    try:
        # Try importing 'question_model' to see if there are any import errors
        import question_model
    except Exception as e:
        assert False, f"Error in question_model.py: {e}"

def test_quiz_brain_execution():
    try:
        # Try importing 'quiz_brain' to see if there are any import errors
        import quiz_brain
    except Exception as e:
        assert False, f"Error in quiz_brain.py: {e}"