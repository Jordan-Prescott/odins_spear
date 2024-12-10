import os
import importlib
import inspect

# Get the directory path of this __init__.py file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Iterate over files in the directory
for filename in os.listdir(current_dir):
    # Skip __init__.py, __pycache__, and non-Python files
    if (
        filename == "__init__.py"
        or filename.startswith("__")
        or not filename.endswith(".py")
    ):
        continue

    module_name = filename[:-3]  # remove the .py extension

    # Dynamically import the module
    module = importlib.import_module(f".{module_name}", package=__name__)

    # Check if there is a function named 'main' in the module
    if hasattr(module, "main") and inspect.isfunction(module.main):
        # Add it to the current package's namespace with the module_name as the attribute name
        globals()[module_name] = module.main
