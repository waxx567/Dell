# Removing the brackets and allowing for an undetermined number of args
def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)


if __name__ == "__main__":
    main()


# python yell03.py
# THIS IS CS50