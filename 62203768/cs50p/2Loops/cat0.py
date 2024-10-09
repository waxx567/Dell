# Ways to meow 3 times
# Using 4 lines
i = 0
while i < 3:
    print("meow")
    i += 1
# Prints a space so output is more readable
print()
# Using 2 lines
for i in [0, 1, 2]: # OR better said - for i in range(3):
    print("meow")
# Space
print()
# Using 1 line
print("meow\n" * 3, end="")