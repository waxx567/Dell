import csv

# Initialise titles array as dictionary
titles = {}

# Read csv file
with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    # Skip first row (headings)
    next(reader)
    # Iterate over titles
    for row in reader:
        # Strip white space and force everything to uppercase
        title = row["title"].strip().upper()
        # Put title in dictionary if not seen before
        if not title in titles:
            titles[title] = 0
        # Add one for this iteration
        titles[title] += 1

# Function returns the value as dictionaries will default print the key first and we want to print titles in order of popularity
#def get_value(title):
#    return titles[title]
#This function is replaced by the lambda function below. They both do exactly the same thing.

# Print keys and values sorting by value and in reverse order (largest to smallest)
for title in sorted(titles, key=lambda title: titles[title], reverse=True):
    print(title, titles[title])