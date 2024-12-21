''' 
In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time,
each time informing the user of the amount due. Once the user has inputted at least 50 cents,
output how many cents in change the user is owed. Assume that the user will only input integers,
and ignore any integer that isn’t an accepted denomination.
'''

# Variable to store amount paid
paid = 0

# Variable to store amount owed
owed = 50

# Keep prompting user until the amount paid reaches the amount owed
while paid < owed:

    # Prompt user to pay
    add = int(input("Insert coin: "))

    # Add amount added added to amount paid
    paid += add

    # Print amount due
    print(f"Amount Due: {owed - paid}")

# Subtract amount owed from amount paid
change = paid - owed

# Print change owed
print(f"Change Owed: {change}")




