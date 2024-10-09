''' 
In a file called playback.py, implement a program in Python that prompts the user for input and then
outputs that same input, replacing each space with ... (i.e., three periods).
'''

# Prompt user for input and store it in text variable
text = input("Text: ")

# Loop through the text searching for spaces
for char in text:
    # Print ellipses if space found
    if char in [" "]:
        print(f"...", end="")
    # Print original character if space not found
    else:
        print(char, end="")

# Go to new line
print()