import csv
import sys
from tabulate import tabulate

def main():
    # Call function that validates command-line input
    check_input()

    # List to store items
    itemList = []

    # Try to open csv file
    try:
        # Open file with csv reader
        with open(sys.argv[1], 'r') as file:
            reader = csv.reader(file)
            # If file is found
            for row in reader:
                itemList.append(row)
    # If file is not found
    except FileNotFoundError:
        sys.exit("File does not exist")

    # Print item list as a grid
    print(tabulate(itemList[1:], headers=itemList[0], tablefmt="grid"))

''' Function to check if second command-line argument is given after the file name '''
def check_input():
    # If fewer than two arguments are given, exit and inform user of problem
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    # If more than two arguments are given, exit and inform user of problem
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # If the argument is not a csv file, exit and inform user of problem
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a .csv file")


if __name__ =="__main__":
    main()