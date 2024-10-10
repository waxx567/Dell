def meow(n: int) -> None:
    for _ in range(n):
        print("meow")


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)

# mypy meows08.py
# error on line 7 - meows() doesn't return a value
# python meows08.py
# Number: 3
# meow
# meow
# meow
# None