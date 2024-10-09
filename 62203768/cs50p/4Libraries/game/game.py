# I’m thinking of a ranInt between 1 and 100… What is it?
# In a file called game.py, implement a program that: Prompts the user for a level, n
# If the user does not input a positive integer, the program should prompt again.
# Randomly generates an integer between 1 and
# , inclusive, using the random module.
# Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.

#     If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
#     If the guess is larger than that integer, the program should output Too large! and prompt the user again.
#     If the guess is the same as that integer, the program should output Just right! and exit.



# import libraries
import random
import sys

# until correct input is received
while True:
    try:
        # get positive integer from user
        # if so, leave while loop
        level = int(input("Level: "))
        if level > 0:
            break
    # not a positive integer
    except:
        # return to top of loop
        continue

# generate random integer - user input as upper bound
ranInt = random.randint(1, level)

# until correct input is received
while True:
    # get guess from user
    try:
        guess = int(input("Guess: "))
        if guess > 0 and guess <= 100:
            if guess < ranInt:
                print("Too small!")
                # return to try loop
                continue
            elif guess > ranInt:
                print("Too large!")
                # return to try loop
                continue
            elif guess == ranInt:
                print("Just right!")
                # exit while loop
                break
    # guess not equal to random integer
    except:
        # return to try loop
        continue