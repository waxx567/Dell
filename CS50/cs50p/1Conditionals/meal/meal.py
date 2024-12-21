''' 
In meal.py, implement a program that prompts the user for a time and
outputs whether it’s breakfast time, lunch time, or dinner time.
If it’s not time for a meal, don’t output anything at all.
Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##.
And assume that each meal’s time range is inclusive.
For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

Structure your program per the below, wherein convert is a function (that can be called by main)
that converts time, a str in 24-hour format, to the corresponding number of hours as a float.
For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).
'''

import sys

def main():

    # Prompt user and store answer in variable
    time_in = input("What time is it? ")

    # Call function on variable and store return value in aariable
    time_out = convert(time_in)

    # Check value and output result
    if (time_out >= 7 and time_out <= 8 ):
        print("breakfast time")
    elif (time_out >= 12 and time_out <= 13):
        print("lunch time")
    elif (time_out >= 18 and time_out <= 19):
        print("dinner time")
    else:
        sys.exit()


# Function to return input time as a percentage
def convert(time):

    # Parse input
    hours, minutes = time.split(":")

    # Work out percentage
    percentage = float(minutes) / 60

    # Return result
    return float(hours) + percentage


# Call main function
if __name__ == "__main__":
    main()