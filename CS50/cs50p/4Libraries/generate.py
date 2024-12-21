# VERSION 1
import random
# VERSION 2
#from random import choice
# VERSION 1
#coin = random.choice(["heads", "tails"])
# VERSION 2
#coin = choice(["heads", "tails"])
#print(coin)
# VERSION 2 has a much shorter runtime

# Function random.randint(a, b) Gets back a random integer between a and b inclusive
#number = random.randint(1, 10)
#print(number)

# Function random.shuffle(x)
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)