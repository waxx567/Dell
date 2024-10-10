# **kwargs accepts any number of keyword arguments
def complicated_function(*args, **kwargs):
    print(args, kwargs)
    pass

complicated_function(x = 1, s = "hello", b = True)
# () {'x': 1, 's': 'hello', 'b': True}

# So to access a particular keyword argument
def complicated_function(*args, **kwargs):
    print(args, kwargs["x"])
    pass

complicated_function(x = 1, s = "hello", b = True)
# () 1

# Useful when you want to make your functions dynamic and you don't know how many regular arguments or keyword arguments you are going to be accepting

# Obviously you can pass both
def complicated_function(*args, **kwargs):
    print(args, kwargs)
    pass

complicated_function(1, 2, 3, x = 1, s = "hello", b = True)
# (1, 2, 3) {'x': 1, 's': 'hello', 'b': True}