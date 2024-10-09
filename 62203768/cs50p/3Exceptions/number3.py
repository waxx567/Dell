# Refining the function

def main():
#       Now main asks the user for input
    x = get_int("x: ")
#       Print output inputting return value from function
    print(f"x is {x}")

# Add prompt to input field of function
def get_int(prompt):
#       Function to handle errors in user input
    while True:
#           Induce an infinite loop so that user keeps getting prompted instead of exiting program after erroneous input
#           Try user input
        try:
#               x = int(input("x: "))
#               return x
#               OR
#               If correct input
            return int(input(prompt))
#           If not int
        except ValueError:
#               Pass to go back into loop
            pass


main()