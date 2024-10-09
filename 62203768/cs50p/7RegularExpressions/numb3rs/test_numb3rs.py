from numb3rs import validate

def test_numb3rs_format():
    assert validate(r"0.0.0.0") == True
    assert validate(r"1.1.1") == False
    assert validate(r"2.2") == False
    assert validate(r"3") == False
    assert validate(r"cat") == False

def test_numb3rs_range():
    assert validate(r"0.0.0.0") == True
    assert validate(r"127.0.0.1") == True
    assert validate(r"255.255.255.255") == True
    assert validate(r"512.512.512.512") == False
    assert validate(r"0.512.1.2") == False
    assert validate(r"0.1.512.2") == False
    assert validate(r"0.1.2.512") == False