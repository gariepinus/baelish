import baelish.currency.quantity

def test_abbrev():
    qty = baelish.currency.quantity.Quantity(5, "Meter", "m")
    assert "{}".format(qty) == "5 m"

def test_long():
    qty = baelish.currency.quantity.Quantity(8, "Euro", "€")
    assert qty.__str__(use_abbrev=False) == "8 Euro"

def test_format():
    qty = baelish.currency.quantity.Quantity(-42.23, "Kilowatt", "kW")
    assert qty.__str__(format_specifier=".2f") == "-42.23 kW"

def test_num():
    qty = baelish.currency.quantity.Quantity(100.4444, "Terabyte", "TB")
    assert qty == 100.4444
