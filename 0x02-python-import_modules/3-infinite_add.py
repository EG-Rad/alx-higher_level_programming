#!/usr/bin/python3
import sys

# Initialize a variable to store the sum
sum_result = 0

# Iterate over command-line arguments (excluding the script name)
for arg in sys.argv[1:]:
    # Convert the argument to an integer and add it to the sum
    sum_result += int(arg)

# Print the sum
print(sum_result)
