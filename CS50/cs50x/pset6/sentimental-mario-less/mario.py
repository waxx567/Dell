# TODO

def main():
    height = get_height()
    for i in range(1, height + 1):

        space = height - i

        print(" " * space, end="")
        print("#" * i)

def get_height():
    while True:
        try:
            n = int(input("Height: "))
            if n >= 1 and n <= 8:
                break
        except ValueError:
            print("That's not an integer!")
    return n

main()