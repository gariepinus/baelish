"""Tests for Amount class."""
import pytest
import baelish.currency


def test_exceptions():
    """Assert Quantity raises TypeErrors when non-ints get passed to num."""
    with pytest.raises(TypeError):
        baelish.currency.Amount(silver_stags=0.5)
    amt = baelish.currency.Amount()
    with pytest.raises(TypeError):
        amt.gold_dragons = 7.4


def test_str():
    """Assert the str method works as intendet."""
    amt = baelish.currency.Amount()
    assert f"{amt}" == "0 CP"
    amt = baelish.currency.Amount(gold_dragons=1)
    assert f"{amt}" == "1 GD"
    amt = baelish.currency.Amount(0, 20, 0)
    assert f"{amt}" == "20 SS"
    amt = baelish.currency.Amount(0, 0, -33)
    assert f"{amt}" == "-33 CP"
    amt = baelish.currency.Amount(5, 100, 0)
    assert f"{amt}" == "5 GD, 100 SS"
    amt = baelish.currency.Amount(1, 0, 20)
    assert f"{amt}" == "1 GD, 20 CP"
    amt = baelish.currency.Amount(0, 50, 1)
    assert f"{amt}" == "50 SS, 1 CP"


def test_getset_gd():
    """Assert getter and setter for property gold_dragons work as intendet."""
    amt = baelish.currency.Amount()
    amt.gold_dragons = -1000
    assert int(amt.gold_dragons) == -1000
    assert f"{amt.gold_dragons}" == "-1,000 GD"


def test_getset_ss():
    """Assert getter and setter for property silver_stags work as intendet."""
    amt = baelish.currency.Amount()
    amt.silver_stags = 666
    assert int(amt.silver_stags) == 666
    assert f"{amt.silver_stags}" == "666 SS"


def test_getset_cp():
    """Assert getter and setter for property copper_pennies work as intendet."""
    amt = baelish.currency.Amount()
    amt.copper_pennies = 3
    assert int(amt.copper_pennies) == 3
    assert f"{amt.copper_pennies}" == "3 CP"


def test_convert_cp():
    """Assert that conversion of whole amount in cp works as intendet."""
    amt = baelish.currency.Amount(0, 1, 80)
    assert int(amt.in_cp) == 136
    amt = baelish.currency.Amount(1, 0, 0)
    assert int(amt.in_cp) == 11760
    amt = baelish.currency.Amount(0, -1, 56)
    assert int(amt.in_cp) == 0


def test_comparsion():
    """Assert that compartion methods work as intended."""
    amt_a = baelish.currency.Amount(silver_stags=1)
    amt_b = baelish.currency.Amount(gold_dragons=1)
    assert amt_a < 57
    assert not amt_a < 56
    assert amt_b < 12000
    assert not amt_b < -0.5
    assert amt_a < amt_b
    assert not amt_b < amt_a

    assert amt_a <= 57
    assert amt_a <= 56
    assert not amt_a <= 3
    assert amt_a <= amt_b

    assert amt_a == 56
    assert amt_b == 11760
    assert not amt_a == amt_b

    assert amt_a != "Foo"
    assert amt_b != -3.33
    assert amt_a != amt_b
