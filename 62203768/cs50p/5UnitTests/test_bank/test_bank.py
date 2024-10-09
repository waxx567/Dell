# Import value function from bank.py
from bank import value

# test return '0'
def test_bank_0():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO WAYNE") == 0

# test return 20
def test_bank_20():
    assert value("hi") == 20
    assert value("Hey") == 20
    assert value("HOWDY") == 20

# test return 100
def test_bank_100():
    assert value("mornimg") == 100
    assert value("Evening") == 100
    assert value("GREETINGS") == 100

# run pytest test_bank.py