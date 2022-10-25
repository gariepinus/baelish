"""Represent a number of coins as an integer."""

class Quantity(int):
    """Integer with unit information."""

    def __new__(cls, num, unit):
        obj = int.__new__(cls, num)
        obj._unit = unit
        return obj

    def __str__(self):
        return f"{int(self)} {self._unit}"
