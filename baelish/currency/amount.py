"""An amount of SIFRP currency represented in Gold Dragons (gd), Silver Stags (ss) and Copper
Pennies (cp)."""
from .quantity import Quantity

class Amount:
    """Three Quiantities of coins."""
    def __init__(self, gold_dragons=0, silver_stags=0, copper_pennies=0):
        self._gold_dragons = Quantity(gold_dragons, "GD")
        self._silver_stags = Quantity(silver_stags, "SS")
        self._copper_pennies = Quantity(copper_pennies, "CP")

    def __repr__(self):
        return f"<Amount: {self._gold_dragons}, {self._silver_stags}, {self._copper_pennies}>"

    def __str__(self):
        if self == 0:
            return "0 CP"
        output=[self._gold_dragons, self._silver_stags, self._copper_pennies]
        return ", ".join(list(map(str, filter(lambda x: int(x) != 0, output))))

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
    def gold_dragons(self):
        """Gold Dragons."""
        return self._gold_dragons

    @gold_dragons.setter
    def gold_dragons(self, value):
        self._gold_dragons.number = value

    @property
    def silver_stags(self):
        """Silver Stags."""
        return self._silver_stags

    @silver_stags.setter
    def silver_stags(self, value):
        self._silver_stags.number = value

    @property
    def copper_pennies(self):
        """Copper Pennies."""
        return self._copper_pennies

    @copper_pennies.setter
    def copper_pennies(self, value):
        self._copper_pennies.number = value

    @property
    def in_cp(self):
        """Whole amount in just copper pennies."""
        value = (int(self._gold_dragons) * (210 * 56)
                + int(self._silver_stags) * 56
                + int(self._copper_pennies))
        return Quantity(value, "CP")

    @property
    def minimized(self):
        """Amount converted in least possible number of coins."""
        original = int(self.in_cp)

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
