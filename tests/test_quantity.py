"""Tests for Quantity"""
import baelish.currency

def test_str():
    """Assert string representation of Quanities works as intended."""
    assert str(baelish.currency.Quantity(5, "CP")) == "5 CP"
    assert str(baelish.currency.Quantity(-3.333, "SS")) == "-3 SS"
    assert str(baelish.currency.Quantity(1000, "GD")) == "1,000 GD"

def test_num():
    """Assert getter and setter for num property work as intended."""
    qty = baelish.currency.Quantity(0, "CP")
    assert qty.num == 0
    qty.num = 6
    assert qty.num == 6

def test_int():
    """Assert integer conversion works as intended."""
    assert int(baelish.currency.Quantity(666, "SS")) == 666
    assert int(baelish.currency.Quantity(-5000, "CP")) == -5000
