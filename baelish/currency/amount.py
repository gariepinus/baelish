"""An amount of SIFRP currency represented in Gold Dragons (gd), Silver Stags (ss) and Copper
Pennies (cp)."""
from .quantity import Quantity

class Amount:
    """Three Quiantities of coins."""
    __gold_dragons = Quantity(0, "GD")
    __silver_stags = Quantity(0, "SS")
    __copper_pennies = Quantity(0, "CP")


    def __init__(self, gold_dragons=0, silver_stags=0, copper_pennies=0):
        self.gold_dragons = gold_dragons
        self.silver_stags = silver_stags
        self.copper_pennies = copper_pennies


    def __repr__(self):
        return f"<Amount: {self.__gold_dragons}, {self.__silver_stags}, {self.__copper_pennies}>"


    def __str__(self):
        if self == 0:
            return "0 CP"
        output=[self.__gold_dragons, self.__silver_stags, self.__copper_pennies]
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
        return self.__gold_dragons


    @gold_dragons.setter
    def gold_dragons(self, value):
        self.__gold_dragons.number = value


    @property
    def silver_stags(self):
        """Silver Stags."""
        return self.__silver_stags


    @silver_stags.setter
    def silver_stags(self, value):
        self.__silver_stags.number = value


    @property
    def copper_pennies(self):
        """Copper Pennies."""
        return self.__copper_pennies


    @copper_pennies.setter
    def copper_pennies(self, value):
        self.__copper_pennies.number = value


    @property
    def in_cp(self):
        """Whole amount in just copper pennies."""
        value = (int(self.__gold_dragons) * (210 * 56)
                + int(self.__silver_stags) * 56
                + int(self.__copper_pennies))
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
