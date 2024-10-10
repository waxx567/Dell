# Operator overloading
class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts


    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"


potter = Vault(100, 50, 25)
print(potter)
# 100 Galleons, 50 Sickles, 25 Knuts

weasley = Vault(25, 50, 100)
print(weasley)
# 25 Galleons, 50 Sickles, 100 Knuts

galleons = potter.galleons + weasley.galleons
sickles = potter.sickles + weasley.sickles
knuts = potter.knuts + weasley.knuts

total = Vault(galleons, sickles, knuts)
print(total)
# 125 Galleons, 100 Sickles, 125 Knuts