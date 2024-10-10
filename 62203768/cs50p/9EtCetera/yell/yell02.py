# Unpacks the list
def main():
    yell(["This", "is", "CS50"])


def yell(words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)
    # this * unpacks the list
    # otherwise the program outputs
    # ['THIS', 'IS', 'CS50']


if __name__ == "__main__":
    main()


# python yell02.py
# THIS IS CS50

# but this yell function only takes one argument (a list in this case) and so it is limited
# if we were to remove the brackets, however, that would leave 3 args and break the program
# this program is not very dynamic