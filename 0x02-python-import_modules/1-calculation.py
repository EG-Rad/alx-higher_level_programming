#!/usr/bin/python3

# Import the functions from calculator_1 module
from calculator_1 import add, sub, mul, div

# Define the values of a and b
a = 10
b = 5

# Perform the calculations and print the results
print("{} + {} = {}".format(a, b, add(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} * {} = {}".format(a, b, mul(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))
