# favorites4.py function replaced with lambda function

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

    # Function for assigning vote counts to loop below
    # def get_value(language):
    #     return counts[language]

    # Iterate over the keys in the dictionary
    # Sort the dictionary by vote count by calling get_value()
    # Reverse the order so that the highest is first
    # for favorite in sorted(counts, key=get_value, reverse=True):
        # Print first the key and then the value
        # print(f"{favorite}: {counts[favorite]}")

    # Iterate over the keys in the dictionary
    # Sort the dictionary by vote count by calling lambda function
    # Reverse the order so that the highest is first
    for favorite in sorted(counts, key=lambda language: counts[language], reverse=True):
        # Print first the key and then the value
       print(f"{favorite}: {counts[favorite]}")