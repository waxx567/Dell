# *args, **kwargs
def f(*args, **kwargs):
    print("Positional: ", args)


f(100, 50, 25)
# python unpack05.py
# # Positional: (100, 50, 25)

f(100, 50, 25, 5)
# python unpack05.py
# Positional: (100, 50, 25, 5)
# No TypeError here as this syntax allows for a flexible number of arguments the function will accept

f(100)
# python unpack05.py
# Positional: (100,)
# This odd looking syntax merely indicates that this tuple is actually a list but with only one element therein