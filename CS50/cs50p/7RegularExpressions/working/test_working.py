'''
Either before or after you implement convert in working.py, additionally implement, in a file called test_working.py, three or more functions that collectively test your implementation of convert thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

pytest test_working.py

'''

from working import convert
import pytest


def test_working_format():
    with pytest.raises(ValueError):
        convert("9:AM - 5:PM")

def test_working_time():
        assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
        assert convert("10 PM to 8 AM") == "22:00 to 08:00"
        assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_working_hour():
    with pytest.raises(ValueError):
        convert("9AM to 13PM")
        convert("13AM to 5PM")

def test_working_minute():
    with pytest.raises(ValueError):
        convert("5:00 AM TO 5:61 PM")
        convert("5:61 AM TO 5:00 PM")

def test_working_range():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
        convert("9:00 AM to 5:60 PM")



if __name__ == "__main__":
    main()