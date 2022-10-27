"""Tests for Quantity"""
import pytest
import baelish.currency


def test_exceptions():
    """Assert Quantity raises TypeErrors when non-ints get passed to num."""
    with pytest.raises(TypeError):
        assert baelish.currency.Quantity(8.7, "GD")
        assert baelish.currency.Quantity(-8.7, "SS")
        assert baelish.currency.Quantity(0.0, "CP")


def test_conversion():
    """Assert Quanity conversion methods work as intended."""
    assert str(baelish.currency.Quantity(5, "CP")) == "5 CP"
    assert str(baelish.currency.Quantity(-3, "SS")) == "-3 SS"
    assert str(baelish.currency.Quantity(1000, "GD")) == "1,000 GD"

    assert int(baelish.currency.Quantity(666, "SS")) == 666
    assert int(baelish.currency.Quantity(-5000, "CP")) == -5000

    assert float(baelish.currency.Quantity(0, "GD")) == 0.0
    assert float(baelish.currency.Quantity(99, "CP")) == 99.0


def test_num():
    """Assert getter and setter for num property work as intended."""
    qty = baelish.currency.Quantity(0, "CP")
    assert qty.number == 0
    qty.number = 6
    assert qty.number == 6
