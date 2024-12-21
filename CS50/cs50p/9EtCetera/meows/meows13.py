# What if we want to handle more inputs than just -n
# docs.python.org/3/library/argparse.html
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n")
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")

# python meows13.py -n 3
# meow
# meow
# meow

# python meows13.py
# TypeError

# python meows13.py -h
# usage: meows13.py [-h] [-n N]
# options:
#   -h, --help  show this help message and exit
#   -n N