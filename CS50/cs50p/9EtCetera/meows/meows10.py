# docstrings
# peps.python.org/pep-0257/
# Python has certain tools built in that detect comments written in this way ("""docstring format""")
# It will assume that the info written within the docstrings is the documentation for the program and we can use tools to analyze and extract these docstrings to generate our documentation (web pages or pdf's) for us without us having to write them up from scratch manually
def meow(n: int) -> str:
    """
    Meow n times.

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * n


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end='')