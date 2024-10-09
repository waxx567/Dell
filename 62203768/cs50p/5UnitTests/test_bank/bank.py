''' Rewritten from bank.py in lect1 '''

def main():
    # Get user input and save in answer string
    answer = input("Greeting: ")
    # Print the result of calling the value function with the user-provided string as input
    print(f"${value(answer)}")


''' Function returns desired values '''
def value(greeting):
    # Strip off whitespace from input and convert string to lowercase
    greeting = greeting.strip().lower()

    ''' Check conditions and return values '''
    # If greeting is "hello"
    if "hello" in greeting:
        return 0
    # If the first letter is 'h'
    elif greeting[0] == 'h':
        return 20
    # All other scenarios
    else:
        return 100


if __name__ == "__main__":
    main()