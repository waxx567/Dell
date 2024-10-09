''' 
In deep.py, implement a program that prompts the user for the answer to the Great Question of Life,
the Universe and Everything, outputting Yes if the user inputs 42 or
(case-insensitively) forty-two or forty two. Otherwise output No.
'''

# Ask user for input
answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")

# Check answer for validity and print relevant result
if answer.strip() == "42" or answer.lower().strip() in ["forty-two", "forty two"]:
    print("Yes")
else:
    print("No")