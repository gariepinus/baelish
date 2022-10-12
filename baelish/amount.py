class Amount:
    """An amount of SIFRP currency represented in Gold Dragons (gd), Silver Stags (ss) and Copper Pennies (cp)."""

    def __init__(self, gd=0, ss=0, cp=0):
        self._goldDragons = Coin("Gold Dragons", "GD", gd)
        self._silverStags = Coin("Silver Stags", "SS", ss)
        self._copperPennies = Coin("Copper Pennies", "CP", cp)

    def __repr__(self):
        return "<Amount: {}, {}, {}>".format(self._goldDragons, self._silverStags, self._copperPennies)

    def __str__(self, useLongUnits=False, maxDecimals=2):
        output=[]

        if self._goldDragons != 0:
            output.append(self._goldDragons.__str__(useLongUnits, maxDecimals))

        if self._silverStags != 0:
            output.append(self._silverStags.__str__(useLongUnits, maxDecimals))

        if self._copperPennies != 0 or (self._goldDragons == 0 and self._silverStags == 0):
            output.append(self._copperPennies.__str__(useLongUnits, maxDecimals))

        return ", ".join(output)

    @property
    def gd(self):
        return self._goldDragons

    @gd.setter
    def gd(self, value):
        self._goldDragons = Coin("Gold Dragons", "GD", value)

    @property
    def ss(self):
        return self._silverStags

    @ss.setter
    def ss(self, value):
        self._silverStags = Coin("Silver Stags", "SS", value)

    @property
    def cp(self):
        return self._copperPennies

    @cp.setter
    def gd(self, value):
        self._copperPennies = Coin("Copper Pennies", "CP", value)


class Coin(float):
    def __new__(self, longUnit, shortUnit, quantity=0):
        return super().__new__(self, quantity)

    def __init__(self, longUnit, shortUnit, quantity=0):
        self._longUnit = longUnit
        self._shortUnit = shortUnit

    def __str__(self, useLongUnit=False, maxDecimals=2):
        return "{} {}".format(round(self, maxDecimals), self._longUnit if useLongUnit else self._shortUnit)
