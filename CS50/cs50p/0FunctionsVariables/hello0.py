# Ask user for name
name = input("What's your name? ")
# Say hello to user
print(f"hello, {name}")
# Another way
print("hello, " + name)
# This one's more verbose but does the same thing
print("hello, ", end="")
print(name)
# Division bar
print("---")
# Users may not input correctly so error correction needed
# Remove whitespace left and right from str variable and force first letter of each word to uppercase
name = name.strip().title()
print(f"hello, {name}")
# Or do all that in one line
# name = input("What's your name? ").strip().upper()
# F string the way to go when printing
# print(f"hello, {name}")