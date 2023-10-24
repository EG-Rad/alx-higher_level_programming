#!/usr/bin/python3
"""
This module defines a Square class.

The Square class represents a square with a private attribute called size.

Attributes:
    size (int): The size of the square.

"""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.

    """
    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.

        """
        self.__size = size
