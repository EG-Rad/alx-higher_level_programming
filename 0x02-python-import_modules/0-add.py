#!/usr/bin/python3

# Assign values to variables a and b
a = 1
b = 2

# Import the add function from add_0 module
from add_0 import add

# Calculate the result using the add function
result = add(a, b)

# Print the result using string formatting
print("{} + {} = {}".format(a, b, result))
