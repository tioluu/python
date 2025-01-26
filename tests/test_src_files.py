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

def test_main_execution():
    # Mock a single input
    inputs = ["true"]
    
    # Mock input and force the program to stop by raising SystemExit
    with patch('builtins.input', side_effect=inputs), patch('sys.exit') as mock_exit:
        try:
            # Try importing and executing the main Python file
            import main  # Adjust if the main function needs to be explicitly called
        except SystemExit:
            pass  # Ignore SystemExit to prevent the test from failing
        except Exception as e:
            assert False, f"Error in main.py: {e}"
        
        # Confirm that the code executed and stopped
        mock_exit.assert_called_once()


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