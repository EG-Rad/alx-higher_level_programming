#!/usr/bin/python3
"""LockedClass module

This module contains the LockedClass class definition.
The LockedClass restricts dynamically creating new instance
attributes except for 'first_name'.

Classes:
    LockedClass: A class that restricts dynamically
    creating new instance attributes.

Example:
    lc = LockedClass()
    lc.first_name = "John"  # Allows setting 'first_name'
    lc.last_name = "Snow"  # Raises an AttributeError due to the restriction
"""


class LockedClass:
    """Class that restricts dynamically creating new instance attributes,
    except 'first_name'."""

    __slots__ = ['first_name']
