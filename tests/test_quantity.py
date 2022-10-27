"""Tests for Quantity"""
import baelish.currency

def test_conversion():
    """Assert Quanity conversion methods work as intended."""
    assert str(baelish.currency.Quantity(5, "CP")) == "5 CP"
    assert str(baelish.currency.Quantity(-3.333, "SS")) == "-3 SS"
    assert str(baelish.currency.Quantity(1000, "GD")) == "1,000 GD"

    assert int(baelish.currency.Quantity(666, "SS")) == 666
    assert int(baelish.currency.Quantity(-5000, "CP")) == -5000

    assert float(baelish.currency.Quantity(0, "GD")) == 0.0
    assert float(baelish.currency.Quantity(99.55, "CP")) == 99.0


def test_num():
    """Assert getter and setter for num property work as intended."""
    qty = baelish.currency.Quantity(0, "CP")
    assert qty.num == 0
    qty.num = 6
    assert qty.num == 6
