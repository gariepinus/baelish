from .quantity import Quantity

class Amount:
    """An amount of SIFRP currency represented in Gold Dragons (gd), Silver Stags (ss) and Copper Pennies (cp)."""

    def __init__(self, gd=0, ss=0, cp=0):
        self._gold_dragons = Quantity(gd, "Gold Dragons", "GD")
        self._silver_stags = Quantity(ss, "Silver Stags", "SS")
        self._copper_pennies = Quantity(cp, "Copper Pennies", "CP")

    def __repr__(self):
        return "<Amount: {}, {}, {}>".format(self._gold_dragons, self._silver_stags, self._copper_pennies)

    def __str__(self, use_abbrev=True, format_specifier=".0f"):
        output=[]

        if self._gold_dragons != 0:
            output.append(self._gold_dragons.__str__(use_abbrev, format_specifier))
        if self._silver_stags != 0:
            output.append(self._silver_stags.__str__(use_abbrev, format_specifier))
        if self._copper_pennies != 0 or (self._gold_dragons == 0 and self._silver_stags == 0):
            output.append(self._copper_pennies.__str__(use_abbrev, format_specifier))
        
        return ", ".join(output)

    def __int__(self):
        return int(self.in_cp)

    def __float__(self):
        return float(self.in_cp)

    def __lt__(self, other):
        return float(self) < float(other)

    def __le__(self, other):
        return float(self) <= float(other)

    def __eq__(self, other):
        return float(self) == float(other)

    def __ne__(self, other):
        return float(self) != float(other)

    def __gt__(self, other):
        return float(self) > float(other)

    def __ge__(self, other):
        return float(self) >= float(other)

    @property
    def gd(self):
        return self._gold_dragons

    @gd.setter
    def gd(self, value):
        self._gold_dragons = Quantity(value, "Gold Dragons", "GD")

    @property
    def in_gd(self):
        return Quantity(self.in_ss / 210, "Gold Dragons", "GD")

    @property
    def ss(self):
        return self._silver_stags

    @ss.setter
    def ss(self, value):
        self._silver_stags = Quantity(value, "Silver Stags", "SS")

    @property
    def in_ss(self):
        return Quantity(self.in_cp / 56, "Silver Stags", "SS")

    @property
    def cp(self):
        return self._copper_pennies

    @cp.setter
    def cp(self, value):
        self._copper_pennies = Quantity(value, "Copper Pennies", "CP")

    @property
    def in_cp(self):
        value = (((self._gold_dragons * 210) + self._silver_stags) * 56) + self._copper_pennies
        return Quantity(value, "Copper Pennies", "CP")

    @property
    def minimized(self):
        original = self.in_cp

        if self < 0:
            original = original * -1
        
        diff = original % (210 * 56)
        gold_dragons = (original - diff) / (210 * 56)

        original = diff
        diff = original % 56
        
        silver_stags = (original - diff) / 56
        copper_pennies = diff

        if self < 0:
            gold_dragons = gold_dragons * -1
            silver_stags = silver_stags * -1
            copper_pennies = copper_pennies * -1

        return Amount(gold_dragons, silver_stags, copper_pennies)
