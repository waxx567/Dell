# Now how to use *args, **kwargs in the function call
def complicated_function(a, b. c = True, d = False):
    pass

# If you tried to pass the list [1, 2] like this
# complicated_function([1, 2])
# It would be the positional argument for a
# but
# complicated_function(*[1, 2])
# will break the list up into two positional arguments - a and b
# thus
# print(a, b)
# 1 2
# same story with keyword arguments
# complicated_function(*[1, 2], {"c": "hi", "d": "ho"})
# will mean the dictionary is c
# but
# complicated_function(*[1, 2], **{"c": "hi", "d": "ho"})
# deconstructs it into it's constituent parts
# so
# print(a, b, c, d)
# 1 2 hi ho