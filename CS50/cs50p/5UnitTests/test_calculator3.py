from calculator import square

def test_square():

    assert square(-3) == 9
    assert square(-2) == 4
    assert square(0) == 0
    assert square(2) == 4
    assert square(3) == 9

# Run pytest test_calculator3.py