# Introducing try/except

# Induce an infinite loop so that user keeps getting prompted instead of exiting program after erroneous input
while True:
# Try user input
    try:
        x = int(input("x: "))
    # If not int
    except ValueError:
        print("x is not an integer")
    # Break out of loop once input is correct (ie. an integer)
    else:
        break

# Print output
print(f"x is {x}")