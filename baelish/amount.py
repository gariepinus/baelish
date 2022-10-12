class Amount:
    """An amount of SIFRP currency represented in Gold Dragons (gd), Silver Stags (ss) and Copper Pennies (cp)."""

    def __init__(self, gd=0, ss=0, cp=0):
        self.gold_dragons = Coin("Gold Dragons", "GD", gd)
        self.silver_stags = Coin("Silver Stags", "SS", ss)
        self.copper_pennies = Coin("Copper Pennies", "CP", cp)

    def __repr__(self):
        return "<Amount: {}, {}, {}>".format(self.gold_dragons, self.silver_stags, self.copper_pennies)

    def __str__(self, useLongUnits=False, format_specifier=".2g"):
        output=[]

        if self.gold_dragons != 0:
            output.append(self.gold_dragons.__str__(useLongUnits, format_specifier))

        if self.silver_stags != 0:
            output.append(self.silver_stags.__str__(useLongUnits, format_specifier))

        if self.copper_pennies != 0 or (self.gold_dragons == 0 and self.silver_stags == 0):
            output.append(self.copper_pennies.__str__(useLongUnits, format_specifier))

        return ", ".join(output)


class Coin(float):
    def __new__(self, longUnit, shortUnit, quantity=0):
        return super().__new__(self, quantity)

    def __init__(self, longUnit, shortUnit, quantity=0):
        self._longUnit = longUnit
        self._shortUnit = shortUnit

    def __str__(self, useLongUnit=False, formatSpecifier=".2g"):
        return "{:{formatSpecifier}} {}".format(self, self._longUnit if useLongUnit else self._shortUnit, formatSpecifier=formatSpecifier)
