import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create object to read file
    reader = csv.DictReader(file)

    # Create a new variable and set it equal to an empty dictionary
    counts = {}

    # Iterate over CSV file, adding to vote scores as necessary
    for row in reader:
        # Select the language column
        favorite = row["language"]
        # If the current language is in the dictionary
        if favorite in counts:
            # Add 1 to that language's tally
            counts[favorite] += 1
        # If the current language is not in the dictionary
        else:
            # Add it to the dictionary and set that language's tally to 1
            counts[favorite] = 1

    # Iterate over the keys in the dictionary
    for favorite in counts:
        # Print first the key and then the value
        print(f"{favorite}: {counts[favorite]}")

    # If you wanted to print in reverse order
    # for favorite in sorted(counts, reverse=True):
    #     print(f"{favorite}: {counts[favorite]}")