# To manipulate data from one file and write the outcome to a second file

import sys
import csv

def main():

    # Validate user input
    check_args()

    dataList = []

    # Try to open files
    try:
        # File to read from
        with open(sys.argv[1], 'r') as inFile:
            reader = csv.DictReader(inFile)
            for row in reader:
                # Parse name on comma
                parseName = row["name"].split(',')
                # Add data to data list removing whitespace from parsing
                dataList.append({"first": parseName[1].lstrip(), "last": parseName[0], "house": row["house"]})
    # If CSV file is not found
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    # File to write to
    with open(sys.argv[2], 'w') as outFile:
        writer = csv.DictWriter(outFile, fieldnames=["first", "last", "house"])
        # Write title row
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        # Transfer information from data file to out file
        for row in dataList:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})


''' Function to check validity of command-line arguments '''
def check_args():

    # Ensure correct number of command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # Ensure CSV files are specified
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()