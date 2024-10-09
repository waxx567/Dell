# Command-Line Arguments
import sys
# This is what we want, that the user supplies the correct command-line arguments for the program to run
#print("hello, my name is", sys.argv[1])
# But suppose the user does not comply
# The above line would trigger an index error if no argument were given after name.py (which is sys.argv[0])
""" CHECKS FOR COMMAND-LINE ARGUMENT FOLLOWING PROGRAM NAME
try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
"""
"""
# CHECKS FOR TOO FEW OR TOO MANY
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])
"""
# Which is all correct code, but there's something about keeping your error checking separate
# From the code you really care about (hence separating them below)
"""
# Check for errors
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
# Print name tag
print("hello, my name is", sys.argv[1])
# BUT If run without a sys.argv[1], gives a NameError even though it
# Still runs the Too few arguments exception notice
"""
# SO
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
print("hello, my name is", sys.argv[1])
# The program is going to sys.exit() at the bottom anyway, this just kicks it out earlier if need be
# Running python name.py "David Malan" in the terminal would result in output of
#hello, my name is David Malan