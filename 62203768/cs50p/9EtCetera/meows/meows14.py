import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", help="number of times to meow")
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")

# python meows14.py
# TypeError

# python meows14.py -h
# usage: meows14.py [-h] [-n N]
# Meow like a cat
# options:
#   -h, --help  show this help message and exit
#   -n N        number of times to meow