def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

print(total(coins[0], coins[1], coins[2]), "Knuts")

# python unpack02.py
# 50775 Knuts

# You couldn't do:

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

print(total(coins), "Knuts")

# because then you would be trying to pass the coins list to total(galleons) without sickles or knuts
# As none of those parameters have defaults (as in sickles=0, knuts=0), they do not accept nothing as arguments
# total() is alsoexpecting an int, not a list
# TypeError: missing positional arguments