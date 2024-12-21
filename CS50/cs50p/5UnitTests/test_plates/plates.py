''' From plates.py in lect2 '''

def main():
    # Get user input
    plate = input("Plate: ")
    # Call is_valid function using requested plate input and output result
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


''' Function to check validity of user input '''
def is_valid(s):

    # Plate must be 2 characters minumum and 6 characters maximum
    if len(s) < 2 or len(s) > 6:
        return False

    # 1st two characters must both be letters
    if not s[0].isalpha() and not s[1].isalpha():
        return False

    # Use a while loop to check if letters follow numbers
    # Assign counter for loop iteration
    i = 0
    # Loop through user input string
    while i < len(s):
        # If the character is a number
        if s[i].isdigit():
            # The first character is zero
            if s[i] == '0':
                return False
            # The first character is a number that is not zero
            else:
                # Return to while loop
                break

        # Increment counter
        i += 1

    # Letters may not follow numbers
    # loop through input string
    for x in range(len(s)):
        # If current character is a number
        if s[x].isdigit():
            # If the next character is not a number
            if not s[x:].isdigit():
                return False

    # Loop through input string
    for char in s:
        # If incorrect character present
        if char in ['.', ',', '!', '?', ' ']:
            return False

    # If none of the above returned False
    return True


if __name__ == "__main__":
    main()