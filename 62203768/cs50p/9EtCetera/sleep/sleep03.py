# Generators, iterators, yield
def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    flock = []
    for i in range(n):
        flock.append('🐑' * i)
    return flock

if __name__ == "__main__":
    main()


# python sleep03.py
# What's n? 3
# 🐑
# 🐑🐑
# 🐑🐑🐑

# ok for 3 or 10 or 100 or 1000, even 10000 sheep
# but it will stop working at a point
# for instance 1 million sheep won't work
# either reaches memory or computing power limit
# this is because the program is trying to return all 1 million sheep (the whole flock) at once