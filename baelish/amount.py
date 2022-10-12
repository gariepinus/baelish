class Amount:
    """An amount of SIFRP currency represented in Gold Dragons (gd), Silver Stags (ss) and Copper Pennies (cp)."""

    def __init__(self, gd=0, ss=0, cp=0):
        self.gold_dragons = gd
        self.silver_stags = ss
        self.copper_pennies = cp

    def __repr__(self):
        return "<Amount: {} GD, {} SS, {} CP>".format(self.gold_dragons, self.silver_stags, self.copper_pennies)

    def __str__(self, format_specifier=".2f"):
        output=[]

        if self.gold_dragons != 0:
            output.append("{:{format_specifier}} GD".format(self.gold_dragons, format_specifier=format_specifier))

        if self.silver_stags != 0:
            output.append("{:{format_specifier}} SS".format(self.silver_stags, format_specifier=format_specifier))

        if self.copper_pennies != 0 or (self.gold_dragons == 0 and self.silver_stags == 0):
            output.append("{:{format_specifier}} CP".format(self.copper_pennies, format_specifier=format_specifier))

        return ", ".join(output)
