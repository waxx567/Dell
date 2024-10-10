def complicated_function(x, y, z = None):
    print(x, y, z)
    pass

complicated_function(1, 2, 3)
# 1 2 3
complicated_function(z = 3, y = 2, x = 1)
# 1 2 3
#  Allows you to no longer pass the parameters positionally
complicated_function(1, z = 3, y = 2)
# 1 2 3
# You can pass some positionally and others using a named argument
# If you try to run
# complicated_function(z = 3, 1, y = 2)
# you will get a SyntaxError: positional argument follows keyword argument because you are not allowed to do that

# NB. Inside the function call, they are referred to as arguments and inside the function itself, they are called parameters

complicated_function(1, 2)
# 1 2 None
# Because the '= None' means z is optional
# This would throw a TypeError if the = None was not there because it would be missing a positional argument
# Run print(x, y)
# if you only want to return
# 1 2