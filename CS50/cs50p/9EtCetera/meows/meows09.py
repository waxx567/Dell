# The solution is to have the function return a value
def meow(n: int) -> str:
    return "meow\n" * n


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end='')

# python meows09.py
# Number: 3
# meow
# meow
# meow