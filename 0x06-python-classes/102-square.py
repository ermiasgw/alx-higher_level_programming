#!/usr/bin/python3
"""Simple square class with his size as a field"""


class Square:
    """Simple square class with his size as a field"""

    def __init__(self, size=0):
        """ Instance the class Square
            Arguments:
                @size: the size of every side of the Square,
                        it must be a positive integer value"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """ Getter for the field size as a property
            Return:
                Value of size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Setter for the field size as a property.
            Arguments:
                @value: the value of size
                        that must be a positive integer value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """Dunders to compare two Square instances:
        eq: to check if are equal
        ne: to check if are not equal
        lt: to check if self is lower
        gt: to check if self is greater
        le: to check if self is lower or equal
        ge: to check if self is greater or equal"""

    def __eq__(self, other):
        return (self.size == other.size)

    def __ne__(self, other):
        return (self.size != other.size)

    def __lt__(self, other):
        return (self.size < other.size)

    def __gt__(self, other):
        return (self.size > other.size)

    def __le__(self, other):
        return (self.size <= other.size)

    def __ge__(self, other):
        return (self.size >= other.size)

    def area(self):
        """ Compute the area of a square
            with the formula:
                                area = @size ^ 2 = @size * @size
            Return:
                    Power of the Square size to 2 or
                    size multiplicated by size."""
        return (self.__size ** 2)
