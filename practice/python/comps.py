# Populate a list with a hundred zeros
x = [0 for i in range(100)]
print(x)
# or 1 to 100
x = [i + 1 for i in range(100)]
print(x)
# evens
x = [i for i in range(100) if i % 2 == 0]
print(x)
# Add another for loop
x = [i*j for i in range(3) for j in range(3)]
print(x)
# Nested for loop for a 2D array
x = [[0 for _ in range(5)] for _ in range(5)]
print(x)
# Can also do with tuple, list
x = (i for i in "hello")
print(x)
# generator object so
print(list(x))
# or
x = (i for i in "hello")
print(tuple(x))
# And dict
words = "hello, my name is .."
x = {char: words.count(char) for char in set(words)}
# In x = {char: words.count(char) for char in set(words)}
# The set(words) gets all the unique letters from the words
# Then for char is for looping through them and
# Then for every single one (char:)
# Count how many times they occur in sentence (words.count(char))
print(x)