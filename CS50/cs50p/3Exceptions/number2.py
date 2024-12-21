# Define a function if you are going to ask for an integer frequently

def main():
    x = get_int()
#       Print output inputting return value from function
    print(f"x is {x}")

def get_int():
#       Function to handle errors in user input
    while True:
#           Induce an infinite loop so that user keeps getting prompted instead of exiting program after erroneous input
#           Try user input
        try:
#               x = int(input("x: "))
#               return x
#               OR
            return int(input("x: "))
#           If not int
        except ValueError:
#               Pass to go back into loop
            pass


main()