import re
import sys


def main():
    # Get user input , send through count function, and print result
    print(count(input("Text:  ")))


# Function to count ums
def count(s):
    ums = re.findall(r"\b\W*um\W*", s, re.IGNORECASE)
    return len(ums)


if __name__ == "__main__":
    main()