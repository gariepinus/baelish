class Amount:
    """An amount of SIFRP currency represented in Gold Dragons (gd), Silver Stags (ss) and Copper Pennies (cp)."""

    def __init__(self, gd=0, ss=0, cp=0):
        self._goldDragons = Coin("Gold Dragons", "GD", gd)
        self._silverStags = Coin("Silver Stags", "SS", ss)
        self._copperPennies = Coin("Copper Pennies", "CP", cp)

    def __repr__(self):
        return "<Amount: {}, {}, {}>".format(self._goldDragons, self._silverStags, self._copperPennies)

    def __str__(self, useLongUnits=False, format_specifier=".2g"):
        output=[]

        if self._goldDragons != 0:
            output.append(self._goldDragons.__str__(useLongUnits, format_specifier))

        if self._silverStags != 0:
            output.append(self._silverStags.__str__(useLongUnits, format_specifier))

        if self._copperPennies != 0 or (self._goldDragons == 0 and self._silverStags == 0):
            output.append(self._copperPennies.__str__(useLongUnits, format_specifier))

        return ", ".join(output)


class Coin(float):
    def __new__(self, longUnit, shortUnit, quantity=0):
        return super().__new__(self, quantity)

    def __init__(self, longUnit, shortUnit, quantity=0):
        self._longUnit = longUnit
        self._shortUnit = shortUnit

    def __str__(self, useLongUnit=False, formatSpecifier=".2g"):
        return "{:{formatSpecifier}} {}".format(self, self._longUnit if useLongUnit else self._shortUnit, formatSpecifier=formatSpecifier)
