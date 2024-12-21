# rewriting of twttr.py from lect2

def main():

    # get input, send input through function, print output

    # prompt user for string as input and save in variable
    inString = input("Input:  ")
    # assign function teturn value to variable
    outString = shorten(inString)
    # print result of calling function
    print(f"Output: {outString}")


# function to remove vowels from input string
def shorten(word):

    # open empty output string
    newString = ""

    # iterate over input string
    for letter in word:
        # convert input to lowercase and check for vowels
        if not letter.lower() in ['a', 'e', 'i', 'o', 'u']:
            # if x is not a vowel, concatenate it to the existing string
            newString += letter

    # return function output string
    return newString


if __name__ == "__main__":
    main()