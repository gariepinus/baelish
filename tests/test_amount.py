import baelish.currency.amount

def test_str_empty():
    amt = baelish.currency.amount.Amount()
    assert "{}".format(amt) == "0 CP"

def test_str_gd():
    amt = baelish.currency.amount.Amount(1, 0, 0)
    assert amt.__str__(use_abbrev=False, format_specifier=".2f") == "1.00 Gold Dragons"

def test_str_ss():
    amt = baelish.currency.amount.Amount(0, 20, 0)
    assert "{}".format(amt) == "20 SS"

def test_str_cp():
    amt = baelish.currency.amount.Amount(0, 0, -33.666)
    assert "{}".format(amt) == "-34 CP"

def test_str_gdss():
    amt = baelish.currency.amount.Amount(5, 100, 0)
    assert "{}".format(amt) == "5 GD, 100 SS"

def test_str_gdcp():
    amt = baelish.currency.amount.Amount(1, 0, 20)
    assert "{}".format(amt) == "1 GD, 20 CP"

def test_str_sscp():
    amt = baelish.currency.amount.Amount(0, 50, 1)
    assert "{}".format(amt) == "50 SS, 1 CP"

def test_getset_gd():
    amt = baelish.currency.amount.Amount()
    amt.gd = -1000
    assert amt.gd == -1000
    assert "{}".format(amt.gd) == "-1000 GD"

def test_getset_ss():
    amt = baelish.currency.amount.Amount()
    amt.ss = 666
    assert amt.ss == 666
    assert "{}".format(amt.ss) == "666 SS"

def test_getset_cp():
    amt = baelish.currency.amount.Amount()
    amt.cp = 3.14159265359
    assert amt.cp == 3.14159265359
    assert amt.cp.__str__(use_abbrev=False, format_specifier=".3f") == "3.142 Copper Pennies"

def test_convert_gd():
    amt = baelish.currency.amount.Amount(0, 104, 56)
    assert amt.in_gd == 0.5

def test_convert_ss():
    amt = baelish.currency.amount.Amount(2, 30, -14)
    assert amt.in_ss == 449.75

def test_convert_cp():
    amt = baelish.currency.amount.Amount(0, 1, 80)
    assert amt.in_cp == 136
