# Write a Python program to say hello to a user
from cs50 import get_string
# Ask user for input and store in variable
answer = get_string("What's your name? ")

# Print answer
print(f"hello, {answer}")