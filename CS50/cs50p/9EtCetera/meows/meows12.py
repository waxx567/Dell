# What if we want the user to type in something more sophisticated like
# python meows11.py -n 3
# where -n is a switch or flag which semantically means 'this number of times'
# A more reliable way (as opposed to python meows11.py 3) of my program knowing what the 3 means
import sys

if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")
else:
    print("usage: meows.py")

# python meows12.py
# meow

# python meows12.py -n 3
# meow
# meow
# meow