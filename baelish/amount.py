class Amount:
    """An amount of SIFRP currency represented in Gold Dragons (gd), Silver Stags (ss) and Copper Pennies (cp)."""

    def __init__(self, gd=0, ss=0, cp=0):
        self.gold_dragons = gd
        self.silver_stags = ss
        self.copper_pennies = cp

    def __repr__(self):
        return "<Amount: {} GD, {} SS, {} CP>".format(self.gold_dragons, self.silver_stags, self.copper_pennies)

    def __str__(self):
        if self.gold_dragons == 0 and self.silver_stags == 0 and self.copper_pennies == 0:
            return "0 CP"

        if self.gold_dragons != 0:
            gd_num = round(self.gold_dragons, 2)
            gd_str = " GD"
            if self.silver_stags != 0 or self.copper_pennies != 0:
                gd_post = ", "
            else:
                gd_post = ""
        else:
            gd_num = ""
            gd_str = ""
            gd_post = ""

        if self.silver_stags != 0:
            ss_num = round(self.silver_stags, 2)
            ss_str = " SS"
            if self.copper_pennies != 0:
                ss_post = ", "
            else:
                ss_post = ""
        else:
            ss_num = ""
            ss_str = ""
            ss_post = ""

        if self.copper_pennies != 0:
            cp_num = round(self.copper_pennies, 2)
            cp_str = " CP"
        else:
            cp_num = ""
            cp_str = ""

        return "{}{}{}{}{}{}{}{}".format(gd_num, gd_str, gd_post, ss_num, ss_str, ss_post, cp_num, cp_str)
