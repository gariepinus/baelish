class Amount:
    """An amount of SIFRP currency represented in Gold Dragons (gd), Silver Stags (ss) and Copper Pennies (cp)."""

    def __init__(self, gd=0, ss=0, cp=0):
        self.gold_dragons = gd
        self.silver_stags = ss
        self.copper_pennies = cp

    def __repr__(self):
        return "<Amount: {:.0f} GD {:.0f} SS {:.0f} CP>".format(self.gold_dragons, self.silver_stags, self.copper_pennies)
