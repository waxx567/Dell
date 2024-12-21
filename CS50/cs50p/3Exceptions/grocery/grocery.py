# In a file called grocery.py, implement a program that prompts the user for items, one per line,
# until the user inputs control-d (which is a common way of ending one’s input to a program).
# Then output the user’s grocery list in all uppercase, sorted alphabetically by item,
# prefixing each line with the number of times the user inputted that item. No need to pluralize the items.
# Treat the user’s input case-insensitively.
# https://cs50.harvard.edu/python/2022/psets/3/grocery/

# dictionary to store items and count
order = {}

# loop until order terminates
while True:
  try:
    # get input from user
    item = input().lower()
    # check dictionary for item
    if item in order:
      # if yes: add 1 to that item's total
      order[item] += 1
    else:
      # if no: this is the first item with that name
      order[item] = 1
  except EOFError:
    # loop through the order
    for key in sorted(order.keys()):
      # print each row in uppercase and alphabetical order
      print(order[key], key.upper())
    # exit while loop
    break