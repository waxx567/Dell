# Function to tell the total value of someone's vault in Gringotts, the wizarding bank
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts
    # According to the books, this is the formula for converting galleons and sickles to knuts

print(total(100, 50, 25), "Knuts")

# python unpack01.py
# 50775 Knuts