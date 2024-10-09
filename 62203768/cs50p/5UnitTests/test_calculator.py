''' You can import a function (square) from another file (calculator.py) as though it's a library, a so-called nodule '''

from calculator import square

def main():
    test_square()

''' If you change the original file on line 6 to say n + n instead of n * n, then you will get "3 squared does not equal 9" but not "2 squared does not equal 4" when running this test file. This is because 2 * 2 is the same as 2 + 2.
Tests must be robust and take as many corner cases as possible into account. '''

def test_square():
    if square(2) != 4:
        print("2 squared does not equal 4")
    if square(3) != 9:
        print("3 squared does not equal 9")

''' Also note that the code in calculator.py is essentially 2 lines long whereas the test code in this test_calculator.py file is 5 lines long. '''

if __name__ == "__main__":
    main()