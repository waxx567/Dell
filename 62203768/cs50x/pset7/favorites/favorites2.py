import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create object to read file
    reader = csv.DictReader(file)

    # Declare variables
    scratch, c, python = 0, 0, 0

    # Iterate over CSV file, adding to vote scores as necessary
    for row in reader:
        favorite = row["language"]
        if favorite == "Scratch":
            scratch += 1
        elif favorite == "C":
            c += 1
        elif favorite == "Python":
            python += 1

    print(f"Scratch {scratch}")
    print(f"C       {c}")
    print(f"Python  {python}")