'''
Suppose that you’d like to implement a cookie jar in which to store cookies. In a file called jar.py, implement a class called Jar with these methods:

__init__ should initialize a cookie jar with the given capacity, which represents the maximum number of cookies that can fit in the cookie jar. If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.
__str__ should return a str with n 🍪, where n is the number of cookies in the cookie jar. For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"
deposit should add n cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity, though, deposit should instead raise a ValueError.
withdraw should remove n cookies from the cookie jar. Nom nom nom. If there aren’t that many cookies in the cookie jar, though, withdraw should instead raise a ValueError.
capacity should return the cookie jar’s capacity.
size should return the number of cookies actually in the cookie jar, initially 0.
Structure your class per the below. You may not alter these methods’ parameters, but you may add your own methods.

class Jar:
    def __init__(self, capacity=12):
        ...

    def __str__(self):
        ...

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...

'''
class Jar:

    # Initializer
    def __init__(self, capacity=12):

        # Error check
        if capacity < 0:
            raise ValueError("Not a positive integer")
        # Assign to object
        self._capacity = capacity
        self._size = 0

    # The __str__ method represents the class objects as a string
    def __str__(self):
        # Prints number of cookies represented as emoji
        return self.size * '🍪'

    # If cookies are being added to jar
    def deposit(self, n):
        # Error message if over limit
        if n > self.capacity or (self.size + n) > self.capacity:
            raise ValueError("Over the limit")
        # Increment value if not
        self._size += n

    # If cookies are being removed from jar
    def withdraw(self, n):
        # Error message if past bound
        if n > self.size:
            raise ValueError("Exceeds amount of cookies in jar")
        # Decrement value if not
        self._size -= n

    # Turn class attribute into property or managed attribute
    @property
    def capacity(self):
        return self._capacity

    # Turn class attribute into property or managed attribute
    @property
    def size(self):
        return self._size


'''
jar = Jar()
jar.deposit(7)
print(jar)
jar.withdraw(4)
print(jar)
'''