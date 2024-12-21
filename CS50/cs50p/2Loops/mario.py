# Simplest way to print three stacked bricks
print("#")
print("#")
print("#")
print()

# Or
for _ in range(3):
    print("#")
print()

# Using a function
def main():
    print_column(3)

# Calls this function
"""
def print_column(height):
    for _ in range(height):
        print("#")
"""
# Or this one
def print_column(height):
    print("#\n" * height, end="")

main()