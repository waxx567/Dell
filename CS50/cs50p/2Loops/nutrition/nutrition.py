# dictionary to store keys and values for data
fruits = {
  "apple": 130,
  "avocado": 50,
  "banana": 110,
  "cantaloupe": 50,
  "grapefruit": 60,
  "grapes":	90,
  "honeydew melon": 50,
  "kiwifruit": 90,
  "lemon": 15,
  "lime": 20,
  "nectarine": 60,
  "orange": 80,
  "peach": 60,
  "pear": 100,
  "pineapple": 50,
  "plums": 70,
  "strawberries": 50,
  "sweet cherries": 100,
  "tangerine": 50,
  "watermelon": 80
}

# prompt user for item
item = input("Item: ")

# loop through dictionary to find item
for fruit in fruits:
  # remove any whitespace and transform input text to lowercase
  # and check result against dictionary keys
  if fruit == item.strip().lower():
    # output answer
    print(f"Calories: {fruits[fruit]}")

