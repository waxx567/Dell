# Example of list comprehension
def make_even(num):
    if num % 2 != 0:
        return num + 1
    else:
        return num

x = [1, 4, 5, 8, 9]
# Use list comprehension to pass list through and assign to new list in one line
y = [make_even(num) for num in x]
print(y)
