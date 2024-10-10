"""PYTHON COMPREHENSIONS"""

# instead of:

values = []
for x in range(10):
    values.append(x)

# print(values)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# use list comprehension ie. write a for loop inside of a list:

values = [x for x in range(10)]

# for every iteration of `for x in range(10)`, we will add a value for `x`

# print(values)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# so:

values = [x + 1 for x in range(10)]

# print(values)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''Whatever is on the left of the expression is the element we want to add for every single element of the for loop.'''


'''Comprehension condition'''

# Get all the even numbers from 0 to 50

# the slow way:

evens = []
for number in range(50):
    is_even = number % 2 == 0
    if is_even:
        evens.append(number)

# print(evens)
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48

# list comprehension:

evens = [number for number in range(50) if number % 2 == 0]
# adds a condition after the for loop

# print(evens)
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]

'''We're taking the number for number in range 50 only if the number modulo 2 equals 0.'''

"""When populating a list, list comprehensions define the parameters in the same line that is defining the list, making it easier to read than the alternative."""


'''Comprehension with multiple conditions'''

# Filter a given list for strings that begin with 'a' and end with 'y', and add them to a new list

options = ["any", "albany", "apple", "world", "hello", ""]
valid_strings = []

for string in options:
    if len(string) <= 1:
        continue

    if string[0] != "a":
        continue

    if string[-1] != "y":
        continue

    valid_strings.append(string)

# print(valid_strings)
# ['any', 'albany']

valid_strings = [
    string
    for string in options
    if len(string) >= 2
    if string[0] == 'a'
    if string[-1] == 'y'
]

# print(valid_strings)
# ['any', 'albany']

'''Splitting long comprehensions onto separate lines makes them much easier to read'''


'''Multiple list comprehension'''

# Flattening a matrix (list of lists)
# Flatten: have one array that doesn't have any nested lists

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = []

for row in matrix:
    for num in row:
        flattened.append(num)

# print(flattened)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

flattened = [num for row in matrix for num in row]
'''The first for loop is the exterior one, and any after are going to run for every iteration of that loop'''

# print(flattened)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]


'''if/else in a comprehension'''

# Categorize numbers as even or odd

categories = []

for number in range(10):
    if number % 2 == 0:
        categories.append("Even")
    else:
        categories.append("Odd")

# print(categories)
# ['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']

categories = [
    "Even" if x % 2 == 0 else "Odd" for x in range(10)
]

# print(categories)
# ['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']


'''Nested list comprehension'''

# Building a 3D list
# A 5x5x5 matrix - a list inside of a list inside of another list

import pprint

printer = pprint.PrettyPrinter()

lst = []

for a in range(5):
    # Create list 1
    l1 = []
    for b in range(5):
        # Create list 2
        l2 = []
        for num in range(5):
            l2.append(num)
        # Put list 2 inside of list 1
        l1.append(l2)

    # Put list 1 inside of main list
    lst.append(l1)

# printer.pprint(lst)
# prints out array of lists within lists too big to type out

lst = [[[num for num in range(5)] for _ in range(5)] for _  in range(5)]

# printer.pprint(lst)
# prints out array of lists within lists too big to type out


'''Transformation in comprehension'''

# List comp with functions

def square(x):
    return x**2

squared_numbers = [square(x) for x in range(10)]

# One could add conditions that point to other functions

squared_numbers = [square(x) for x in range(10) if valid(x)]
# Would have to write the valid() function, of course


'''Dictionary comprehensions'''

# Creating a dictionary
pairs = [("a", 1), ("b", 2), ("c", 3)]

my_dict = {k: v for k, v in pairs}


# Mimic DNA pairing in code
import random

bases = ['A', 'T', 'C', 'G']
# to generate a strand which is 10 items long
strand1 = random.choices(bases, k=10)
print(strand1)

# given the above, implement the following with dictionary comprehension:
'''
dna = {}

for idx, b in enumerate(dna_st1):
    if b == 'A':
        b2 = 'T'
    elif b == 'T':
        b2 = 'A"
    elif b == 'C':
        b2 = 'G'
    else:
        b2 = 'C'

    dna[idx] = [b, b2]

resulting in a dictionary of 10 random pairs (paired to correct partners) where the index is the key and the pair (list of 2 chars) is the value
the first item is taken out of strand 1 and strand 2 is generated based on strand 1
'''
dna = {
    key:
    [val, ('T' if val == 'A' else 'A' if val == 'T' else 'C' if val == 'G' else 'G')]
    for (key, val) in enumerate(strand1)
    }

print(dna)


# list of dictionaries
import random
import string
# print(string.printable)
# prints a string of all numbers, lower- and uppercase letters,and symbols

keys = ["id", "username", "password"]
users = ["waynem567", "basedCat"]

data = [{} for i in range(len(users))]
# print(data)
# [{}, {}]

data = [{key:
         None
         for key in keys
         } for i in range(len(users))]
# print(data)

data = [{
    key:
    (i if key == "id" else users[i] if key == "username" else None)
    for key in keys
    } for i in range(len(users))]
# print(data)

# To generate random passwords
password = random.choices(string.printable, k=8)
# print(password)
# prints the password, but it is a list of chars

password = ''.join(random.choices(string.printable, k=8))
# print(password)

### copy this code (just the assignment, not the variable) back into the dict comp from above

data = [{
    key:
    (i if key == "id" else users[i] if key == "username" else ''.join(random.choices(string.printable, k=8)))
    for key in keys
    } for i in range(len(users))]
# print(data)

# You can now add new users simply by adding usernames - ids and passwords will be generated automatically


'''Set comprehensions'''

# Removing duplicates from a list while applying a function
nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

unique_squares = {x**2 for x in nums}
'''Python recognizes {} here ^ is a set not a dict because no key has been associated with the value'''