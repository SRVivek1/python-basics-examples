"""
    This program demonstrates basics of enum
"""
from enum import Enum


class Color(Enum):
    """
    Sample Enum class.
    """
    '''Enum properties.'''
    RED = 101
    BLUE = 201
    GREEN = 301


class Flower:
    """
    Flower class use Color enum.
    """

    def __init__(self, color: Color):
        """
        :param color:
        """
        self.c = Color(color)

    def info(self):
        print(f"My color is {self.c}")


# Driver
if __name__ == '__main__':
    obj1 = Flower(Color.RED)
    obj1.info()
