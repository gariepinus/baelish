class Coin(float):
    def __new__(self, longUnit, shortUnit, quantity=0):
        return super().__new__(self, quantity)

    def __init__(self, longUnit, shortUnit, quantity=0):
        self._longUnit = longUnit
        self._shortUnit = shortUnit

    def __str__(self, useLongUnit=False, formatSpecifier=".2f"):
        return "{:{formatSpecifier}} {}".format(self, self._longUnit if useLongUnit else self._shortUnit, formatSpecifier=formatSpecifier)
