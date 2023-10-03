#!/usr/bin/python3
def print_last_digit(number):
    # Calculate the last digit using the modulo operator
    last_digit = abs(number) % 10
    
    # Print the last digit
    print(last_digit, end="")
    
    # Return the last digit
    return last_digit
