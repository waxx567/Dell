# Type hints
def meow(n: int):
    for _ in range(n):
        print("meow")


number = input("Number: ")
meow(number)
# TypeError: 'str' object cannot be interpreted as an integer
# pip install mypy
# mypy meows04.py
# meows4.py:8: error: Argument 1 to "meow" has incompatible type "str"; expected "int"  [arg-type]