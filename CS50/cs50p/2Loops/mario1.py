def main():
    """
    print_row(4)

def print_row(width):
    print("?" * width)
"""
    # Call function plugging in size
    print_square(3)

# Define function
def print_square(size):
    """
    # For each row in square
    for i in range(size):
        # For each brick in row
        for j in range(size):
            # Print brick
            print("#", end="")
        # Moves to new line
        print()
    """

# Rather
    for i in range(size):
        print("#" * size)

main()