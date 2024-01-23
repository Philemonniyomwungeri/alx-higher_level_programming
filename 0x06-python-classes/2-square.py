#!/usr/bin/python3
"""
Module 2-square

This module defines the Square class with a private size attribute and size validation.
"""


class Square:
    """
    Represents a square.

    Attributes:
    - __size (int): The size of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Parameters:
        - size (int): The size of the square (default is 0).

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
