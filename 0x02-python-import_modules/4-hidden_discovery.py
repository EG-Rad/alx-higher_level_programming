#!/usr/bin/python3
import importlib.util
import sys

# Load the compiled module
module_name = 'hidden_4'
module_path = 'hidden_4.pyc'
spec = importlib.util.spec_from_file_location(module_name, module_path)
compiled_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(compiled_module)

# Get the names defined in the module
module_names = [name for name in dir(compiled_module) if not name.startswith("__")]

# Print the names in alphabetical order
for name in sorted(module_names):
    print(name)
