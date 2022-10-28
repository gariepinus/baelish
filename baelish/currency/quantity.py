"""Type for coin quantity properties of Amount.

This module defines a very simple class intendet to describe quantities of coins as a number and
unit (eg. "3 GD") for the different coin quantities in an Amount.
"""


class Quantity():
    """A quantity of coins.

    Attributes:
        num (int): Number of coins
        unit (string): Unit of coins
    """
    def __init__(self, number, unit):
        if not isinstance(number, int):
            raise TypeError("number must be integer")
        if not isinstance(unit, str):
            raise TypeError("unit must be string")
        self.__number = number
        self.__unit = unit


    def __repr__(self):
        return f"<{self.__number} {self.__unit}>"


    def __str__(self):
        return f"{self.__number:,} {self.__unit}"


    def __int__(self):
        return self.__number


    def __float__(self):
        return float(self.__number)


    @property
    def number(self):
        """Number of coins."""
        return self.__number


    @number.setter
    def number(self, value):
        if not isinstance(value, int):
            raise TypeError("number must be integer")
        self.__number = value


    @property
    def unit(self):
        """Unit of coins."""
        return self.__unit
