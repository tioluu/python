import importlib

def test_another_module_import():
    try:
        importlib.import_module("src.another_module.py")
    except Exception as e:
        assert False, f"Error in another_module.py: {e}"

def test_coffee_machine_execution():
    try:
        # Execute Coffee_machine.py as a script
        with open("src/Coffee_machine_d16.py") as f:
            exec(f.read())
    except Exception as e:
        assert False, f"Error in Coffee_machine_d16.py: {e}"
