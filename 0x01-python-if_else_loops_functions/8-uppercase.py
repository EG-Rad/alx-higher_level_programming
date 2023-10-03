def uppercase(s):
    for char in s:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert the lowercase character to uppercase and print it
            uppercase_char = chr(ord(char) - 32)
            print(uppercase_char, end="")
        else:
            # Print characters that are not lowercase letters as they are
            print(char, end="")
    
    # Print a new line after processing the entire string
    print()
