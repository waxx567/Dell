# A better way puts all of the addition insidethe class
class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    # We need to add two Vault objects together
    def __add__(self, other):
        # self refers to whatever object is on the left of the + sign
        # other is whatever object is on the right hand side
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)


potter = Vault(100, 50, 25)
print(potter)
# 100 Galleons, 50 Sickles, 25 Knuts

weasley = Vault(25, 50, 100)
print(weasley)
# 25 Galleons, 50 Sickles, 100 Knuts

total = potter + weasley
print(total)
# 125 Galleons, 100 Sickles, 125 Knuts

# List of operators that you can overload
# docs.python.org/3/reference/datamodel.html#special-method-names