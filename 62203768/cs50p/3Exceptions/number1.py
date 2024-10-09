# Cleaner number.py

while True:

    try:
        # Try to get int from user and store in x
        x = int(input("x: "))
        # Break out if correct input
        break
    except ValueError:
        # If incorrect input
        print("x is not an integer")

print(f"x is {x}")
