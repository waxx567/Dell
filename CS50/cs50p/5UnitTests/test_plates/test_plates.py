from plates import is_valid

# test length
def test_plates_minmax():
    assert is_valid("AA") == True
    assert is_valid("WAYNE1") == True
    assert is_valid("X") == False
    assert is_valid("WAYNE01") == False

# First two characters must be letters
def test_plates_first_two():
    assert is_valid("XY") == True
    assert is_valid("X0") == False
    assert is_valid("1A") == False
    assert is_valid("77") == False

# numbers at end only
def test_plates_numbers_at_end():
    assert is_valid("AA8") == True
    assert is_valid("AAA8") == True
    assert is_valid("AA88") == True
    assert is_valid("AA8A") == False

# 1st number not 0
def test_plates_first_number_not_0():
    assert is_valid("AA80") == True
    assert is_valid("AAA80") == True
    assert is_valid("AA08") == False
    assert is_valid("AAA0") == False

# no periods, spaces, punctuation
def test_plates_invalid_char():
    assert is_valid("WA.YNE") == False
    assert is_valid("WA!YNE") == False
    assert is_valid("WA YNE") == False
    assert is_valid("WA?YNE") == False


''' run pytest test_plates.py '''