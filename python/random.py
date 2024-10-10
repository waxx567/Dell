from random import shuffle, random, randint, randrange, choice, choices, sample, seed

"""shuffle"""
# Create a list of strings called people
people: list[str] = ["Bob", "Tom", "James", "Sandra"]
# Call the random shuffle function on the people list
shuffle(people)
print(people)

"""random"""
# generate a random float called value between 0 and 1 by calling the random function
value: float = random()
print(f"random() = {value}")

"""randint"""
# generate a list of integers called values using 5 randomly chosen numbers between 10 and 20 (both inclusive) by calling the randint function
values: list[int] = [randint(10, 20) for _ in range(5)]
print(f"randint() = {values}")

"""randrange"""
# generate a list of integers called values2 using 5 randomly chosen numbers between 0 and 3 (lower bound inclusive, upper bound exclusive) by calling the randrange function
values2: list[int] = [randrange(0, 3) for _ in range(5)]
print(f"randrange() = {values2}")
# generate a list of integers called values2 using 5 randomly chosen numbers between 0 and 10 (lower bound inclusive, upper bound exclusive) by calling the randrange function, with a step value of 2 between the numbers, starting at 0 (evens)
values2: list[int] = [randrange(0, 10, 2) for _ in range(5)]
print(f"randrange() = {values2}")
# generate a list of integers called values2 using 5 randomly chosen numbers between 0 and 10 (lower bound inclusive, upper bound exclusive) by calling the randrange function, with a step value of 2 between the numbers, starting at 1 (odds)
values2: list[int] = [randrange(1, 10, 2) for _ in range(5)]
print(f"randrange() = {values2}")

"""choice, choices"""
people: list[str] = ["Bob", "Tom", "James", "Sandra"]
# Select 1 random element from a list
print(f"choice() = {choice(people)}")
# Select 3 random elements from a list
print(f"choices() = {choices(people, k=3)}")
"""weights"""
# Weighting the options
weights: tuple = (.15, .20, .35, .30)
# Bob 15%, Tom 20%, James 35%, Sandra 30% (the probabilities of a name coming up)
print(f"choices() = {choices(people, k=6, weights=weights)}")

## choice/choices will return some duplicate elements, sample will return unique elements only

"""sample"""
print(f"sample() = {sample(range(100), k=10)}")
# Returns a list of 10 unique randomly chosen numbers between 0 and 99
# every time you run this, you will get unique numbers because sample removes the ones it has shown and chooses from the remainder
# however if the elements sample chooses from are the same, it will return each one once only
# print(f"sample() repeats = {sample([1, 1, 2, 3], k=10)}")
# would give a value error because you can't ask for more elements than there are in the range or list so
print(f"sample() = {sample([1, 1, 2, 3], k=4)}")

# now
colors: list[str] = ['r', 'g', 'b']
# print(sample(colors), k=5)
# will obviously raise a ValueError because there are only 3 elements, not 5
# but one can multiply the elements using counts
print(sample(colors), k=5, counts=(10, 20, 5))
# so the new list to sample from will contain 10 reds, 20 greens and 5 blues

"""seed"""
'''will save a selected number of random states'''
seed(1)
print(f"{random() = }")
print(f"{randint(1, 5) = }")
print(f"{sample(range(1000), k=5) = }")
# The program will now return the same set of results when re-run