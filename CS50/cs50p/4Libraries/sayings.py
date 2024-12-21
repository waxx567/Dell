def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")

# If you want to import these functions to your other programs (as in say.py)
# You need to
if __name__ == "__main__":
    main()
# As just calling main() would call main function in all circumstances
# Try it and see:
#main()