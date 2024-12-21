# Same but using command-line arguments
import sys

if len(sys.argv) == 1:
    print("meow")
else:
    print("usage: meows.py")

# python meows11.py
# meow

# python meows11.py 3
# usage: meows.py

# which is a common way to tell the user how to use the program