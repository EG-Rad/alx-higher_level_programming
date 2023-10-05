#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

# Check the number of arguments
if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

# Extract the arguments
a = int(sys.argv[1])
operator = sys.argv[2]
b = int(sys.argv[3])

# Perform the calculation based on the operator
if operator == "+":
    result = add(a, b)
elif operator == "-":
    result = sub(a, b)
elif operator == "*":
    result = mul(a, b)
elif operator == "/":
    if b == 0:
        print("Error: Division by zero")
        sys.exit(1)
    result = div(a, b)
else:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

# Print the result
print("{} {} {} = {}".format(a, operator, b, result))

