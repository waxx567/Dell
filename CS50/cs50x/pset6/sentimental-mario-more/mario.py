# TODO

# Program to output a two-sided pyramid of user-defined height


def main():
    # Call function to get height from user
    height = get_height()
    # Iterate that many times starting at 1
    for i in range(1, height + 1):
        # Define a space
        space = height - i

        # Print pyramid
        print(" " * space, end="")
        print("#" * i, end="")
        print("  ", end="")
        print("#" * i)


# Function to get height from user
def get_height():
    while True:
        try:
            # Keep asking
            n = int(input("Height: "))
            # Until user input within range
            if n >= 1 and n <= 8:
                break
        except ValueError:
            # If anything other than an integer is entered
            print("That's not an integer!")
    # Send validated integer back to main
    return n


main()