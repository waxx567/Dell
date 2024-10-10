# Prints a list of words in uppercase
def main():
    yell(["This", "is", "CS50"])


def yell(words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(uppercased)


if __name__ == "__main__":
    main()


# python yell01.py
# ['THIS', 'IS', 'CS50']