# From: https://cs50.harvard.edu/python/2022/psets/5/test_fuel/

from fuel import convert, gauge
import pytest

# Test input
def test_fuel_convert_input():
    assert convert("1/2") == 50 and gauge(50) == "50%"
    assert convert("99/100") == 99 and gauge(99) == "F"
    assert convert("1/100") == 1 and gauge(1) == "E"

# Test zer division error
def test_fuel_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

# Test value error
def test_fuel_value_error():
    with pytest.raises(ValueError):
        convert("one/two")