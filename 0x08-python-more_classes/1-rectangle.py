#!/usr/bin/python3
"""Rectangle module

This module defines the Rectangle class representing a geometric rectangle.

Classes:
    Rectangle: Represents a basic rectangle shape.

"""


class Rectangle:
    """Class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle with a width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value