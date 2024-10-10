import csv
import sys
from cs50 import get_string


def main():
    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: dna.py databases/[FILENAME].csv sequences/[FILENAME].txt")
        sys.exit(1)

    # TODO: Read database file into a variable
    db_file = open(sys.argv[1])
    db_reader = csv.DictReader(db_file)

    # TODO: Read DNA sequence file into a variable
    sq_file = open(sys.argv[2])
    sequences = sq_file.read()
    sq_file.close()

    # Get STR names from database file
    strs = db_reader.fieldnames[1:]

    str_info = {}
    # Call str_repeats() on each STR and store information in str_info dictionary
    for str in strs:
        str_info[str] = str_repeats(str, sequences)

    # Loop over database file
    for row in db_reader:
        # Call match() on each row to compare STRs
        if match(strs, str_info, row):
            # Print name if match found
            print(f"{row['name']}")
            # Close database file
            db_file.close()
            return

    # If no match found
    print("No match")
    db_file.close()

    # TODO: Find longest match of each STR in DNA sequence
    final = longest_match(db_file, sq_file)
    # TODO: Check database for matching profiles

    return


# Take STR name and count repeats of that sequence in sequences file
def str_repeats(str, sequences):
    i = 0
    # If a repeat is found, start counting
    while str * (i + 1) in sequences:
        # Increment if more repeats are found
        i += 1
    # Return number of repeats
    return i


# Function to check STRs for matches
def match(strs, str_info, row):
    # Check each STR
    for str in strs:
        # If STR not in stored information dictionary
        if str_info[str] != int(row[str]):
            return False
    # If match found
    return True


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive count of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive count
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for count at each character in sequence, return longest run found
    return longest_run


main()