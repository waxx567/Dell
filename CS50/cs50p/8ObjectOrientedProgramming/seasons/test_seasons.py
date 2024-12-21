'''
Either before or after you implement seasons.py, additionally implement, in a file called test_seasons.py, one or more functions that test your implementation of any functions besides main in seasons.py thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

pytest test_seasons.py

'''

from seasons import validate


def test_seasons_validate():
    assert validate("1967-05-09") == ("1967", "05", "09")
    assert validate("1967-5-9") == None
    assert validate("May 9, 1967") == None


if __name__ == "__main__":
    main()