# Let's handle the TypeError
import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")

# python meows15.py
# meow

# default specifies that if no second argument is submitted, the program will take the argument as 1 and sent that to args.n (line 8)
# and type specifies that it will be an int

# python meows15.py dog
# usage: meows15.py [-h] [-n N]
# meows15.py: error: argument -n invalid int value: 'dog'