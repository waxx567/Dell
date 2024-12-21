import sys

# To accept multiple name inputs to print many name tags at once
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
for arg in sys.argv[1:]: # sys.argv[1:] means start at element 1 (not 0, which is name.py) and go to the end of the list
    print("hello, my name is", arg)

    