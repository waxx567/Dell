# One of the most popular places to eat in Harvard Square is Felipe’s Taqueria,
# which offers a menu of entrees, per the dict below, wherein the value of each key is a price in dollars:

# dictionary with items and prices
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# store bill total
total = 0

# keep asking for items until order terminated (when Ctrl D is hit)
while True:
    try:
        # prompt user capitalizing the input
        item = input("Item: ").title()
        # if legitimate order, add to total and print
        if item in menu:
            total += menu[item]
            print(f"${total:.2f}")
    # once order is terminated
    except EOFError:
        # print new line
        print()
        # exit loop
        break