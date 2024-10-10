# switches from language to problem
import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create object to read file
    reader = csv.DictReader(file)

    # Create a new variable and set it equal to an empty dictionary
    counts = {}

    # Iterate over CSV file, adding to vote scores as necessary
    for row in reader:
        # Select the problem column
        favorite = row["problem"]
        # If the current problem is in the dictionary
        if favorite in counts:
            # Add 1 to that problem's tally
            counts[favorite] += 1
        # If the current problem is not in the dictionary
        else:
            # Add it to the dictionary and set that problem's tally to 1
            counts[favorite] = 1

    # Iterate over the keys in the dictionary
    # Sort the dictionary by vote count by calling lambda function
    # Reverse the order so that the highest is first
    for favorite in sorted(counts, key=lambda problem: counts[problem], reverse=True):
        # Print first the key and then the value
       print(f"{favorite}: {counts[favorite]}")