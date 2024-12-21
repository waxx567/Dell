# One of David’s first toys as a child, funny enough, was Little Professor, a “calculator” that would generate ten different math problems for David to solve. For instance, if the toy were to display 4 + 0 = , David would (hopefully) answer with 4. If the toy were to display 4 + 1 = , David would (hopefully) answer with 5. If David were to answer incorrectly, the toy would display EEE. And after three incorrect answers for the same problem, the toy would simply display the correct answer (e.g., 4 + 0 = 4 or 4 + 1 = 5).

# In a file called professor.py, implement a program that:

#       Prompts the user for a level, n. If the user does not input 1, 2, or 3, the program should prompt again.
#       Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y
#           is a non-negative integer with digits. No need to support operations other than addition (+).
#       Prompts the user to solve each of those problems. If an answer is not correct (or not even a number),
#           the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem.
#           If the user has still not answered correctly after three tries, the program should output the correct answer.
#       The program should ultimately output the user’s score: the number of correct answers out of 10.

# Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, and generate_integer returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:

# generate random numbers when needed
import random


def main():
    ...
    # call function to get level
    level = get_level()
    # call sums function and save result in score
    score = generate_integer(level)
    # output score
    print("Score: ", score)

# function to validate level from user and return as an integer
def get_level():
    ...
    # prompt user until they return a 1, 2 or 3
    while True:
        try:
            # get input
            level = input("Level: ")
            # input is correct
            if level.isdigit() and int(level) in [1, 2, 3]:
                # return input converted to integer
                return int(level)
        # go back to try
        except ValueError:
            continue

# function to generate sums, validate answers and tally scores
def generate_integer(level):
    ...
    # variable to keep score
    score = 0
    # parameters for sums are determined by level chosen
    if level == 1:
        a = 0
        b = 9
    elif level == 2:
        a = 10
        b = 99
    else:
        a = 100
        b = 999

    # randomly generate the integers for 10 sums to solve
    for i in range(10):
        x = random.randint(a, b)
        y = random.randint(a, b)

        # give 3 chances at each sum
        for j in range(3):
            # prompt user for answer
            answer = int(input(f"{x} + {y} = "))
            # answer is correct
            if answer == x + y:
                # maximize j so that the same sum is not asked again
                j = 2
                # add 1 to score and return to for loop
                score += 1
                break
            # answer is incorrect
            else:
                print("EEE")
                # increment j
                j += 1
                # all chances have been used up
                if j == 3:
                    # print correct answer
                    print(f"{x} + {y} = {x + y}")

    # return final score tally
    return score


if __name__ == "__main__":
    main()