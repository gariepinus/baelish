class Quantity(float):
    """Float with a unit."""

    def __new__(self, num, unit, abbrev):
        return super().__new__(self, num)

    def __init__(self, num, unit, abbrev):
        self._unit = unit
        self._abbrev = abbrev

    def __str__(self, use_abbrev=True, format_specifier=".2f"):
        return "{:{format_specifier}} {}".format(self,
                self._abbrev if use_abbrev else self._unit,
                format_specifier=format_specifier)
