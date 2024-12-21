# TODO

# To handle floating point numbers
from cs50 import get_float


def main():
    change = userin()
    quarters = int(change / 0.25)
    # print(f"Quarters: {quarters}")
    change = change % 0.25
    dimes = int(change / 0.10)
    # print(f"Dimes: {dimes}")
    change = change % 0.10
    nickels = int(change / 0.05)
    # print(f"Nickels: {nickels}")
    change - int(change % 0.1)
    pennies = round((change % 0.01) * 100)
    # print(f"Pennies: {change}")
    coins = quarters + dimes + nickels + pennies
    print(f"{coins}")


# Validate user input
def userin():
    while True:
        try:
            n = float(input("Change owed: "))
            if n > 0.00 and n < 100.00:
                break
        except ValueError:
            print("Please enter amount to 2 (two) decimal places.")
    return n


main()