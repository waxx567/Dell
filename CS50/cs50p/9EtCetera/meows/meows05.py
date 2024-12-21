def meow(n: int):
    for _ in range(n):
        print("meow")


number: int = input("Number: ")
meow(number)

# mypy now finds the problem on line 7