# In a file called fuel.py, implement a program that prompts the user for a fraction,
# formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage
# rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains,
# output E instead to indicate that the tank is essentially empty. And if 99% or more remains,
# output F instead to indicate that the tank is essentially full.
# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.
# (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.

# variables to assign input to
num, den = 0, 0
# prompt user
print("Fraction: ")
# keep prompting user if user input is not correct
while True:
    # try loop ensures program does not break if user input is invalid
    try:
        # prompt again
        fraction = input("Fraction: ")
        # parse input
        num, den = fraction.split("/")
        # convert input strings to integers
        num, den = int(num), int(den)
        # if `num, den = int(num), int(den)` was successful
        if num > den or den == 0:
            # leave if loop
            continue
        # leave while loop
        break
    # if `num, den = int(num), int(den)` was not successful
    # meaning one of the input values was not an integer
    # print an explanatory message to user and return to while loop
    except ValueError:
        print("Usage: X/Y [integer(X) < integer(Y)]")

# calculate percentage amount represented by denominator
fraction = 100 / den
# round the result
percent = round(fraction * num)
# print output
if percent <= 1:
    print("E")
elif percent >= 99:
    print("F")
else:
    print(f"{percent}%")