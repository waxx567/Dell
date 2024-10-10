def complicated_function(x, y, *args):
    print(x, y, args)
    pass

complicated_function(1, 3, 8, 4, 6, 9, 2, 3)
# 1 3 (8, 4, 6, 9, 2, 3)
# Allows me to pass any number of positional arguments after my defined positional arguments and store them in a tuple, which is immutable

# Also

def complicated_function(*args):
    print(args)
    pass
complicated_function(1, 3, 8, 4, 6, 9, 2, 3)
# (1, 3, 8, 4, 6, 9, 2, 3)

# and

def complicated_function(*args):
    print(args)
    pass
complicated_function()
# ()