# Generators, iterators, yield
# generators can generate a massive amount of data for your users but you can have it return just a little bit of that data at a time
# yield returns just one value at a time
def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    for i in range(n):
        yield '🐑' * i


if __name__ == "__main__":
    main()


# python sleep04.py
# What's n? 3
# 🐑
# 🐑🐑
# 🐑🐑🐑

# yield is generating one row of sheep at a time
# yield is returning an iterator that allows our for loop in main to iterate over these generated values one at a time
# the program can now return 1 million sheep