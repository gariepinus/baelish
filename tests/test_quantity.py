"""Tests for the Quantity class"""
import baelish.currency

def test_meter():
    """Assert Quantity "5 m" can be converted to string correctly and the integer value is set
    right."""
    qty = baelish.currency.Quantity(5, "m")
    assert f"{qty}" == "5 m"
    assert qty == 5

def test_num():
    """Assert Quantity "5 TB" can be converted to string correctly and the integer value is set
    right."""
    qty = baelish.currency.Quantity(100.4444, "TB")
    assert f"{qty}" == "100 TB"
    assert qty == 100
