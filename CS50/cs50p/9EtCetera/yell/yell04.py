# map
# in this case replaces 3 lines with 1
def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)


if __name__ == "__main__":
    main()


# python yell04.py
# THIS IS CS50
