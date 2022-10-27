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

    def __init__(self, num, unit):
        if not isinstance(num, int):
            raise TypeError("num must be int.")
        self._num = int(num)
        self._unit = str(unit)

    def __repr__(self):
        return f"<{self._num} {self._unit}>"

    def __str__(self):
        return f"{self._num:,} {self._unit}"

    def __int__(self):
        return self._num

    def __float__(self):
        return float(self._num)

    @property
    def num(self):
        """Number of coins."""
        return self._num

    @num.setter
    def num(self, value):
        if not isinstance(value, int):
            raise TypeError("num must be int.")
        self._num = int(value)
