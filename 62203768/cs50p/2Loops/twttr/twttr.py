''' 
When texting or tweeting, it’s not uncommon to shorten words to save time or space,
as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py,
implement a program that prompts the user for a str of text and then outputs that same text but
with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
'''

# Prompt user
str_in = input("Input:  ")

# Print answer
print(f"Output: ", end="")

# Loop through each character in input string
for char in str_in:
    # For every character that is not a vowel
    if char.lower() not in "aeiou":
        # Print that character and don't go to a new line after doing so
        print(char, end="")

# Go to a new line
print()