def meow(n: int):
    for _ in range(n):
        print("meow")


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)

# python meows07.py
# Number: 3
# meow
# meow
# meow
# None

# because the function is still printing the meows and the final print statement is printing the RETURN VALUE of the function
# The function does not return anything so the value is None