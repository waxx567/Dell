'''
Five hundred twenty-five thousand, six hundred minutes
Five hundred twenty-five thousand moments so dear
Five hundred twenty-five thousand, six hundred minutes
How do you measure, measure a year?

— “Seasons of Love,” Rent

Assuming there are 365 days in a year, there are 365 x 24 x 60 = 525,600
 minutes in that same year (because there are 24 hours in a day and 60 minutes in an hour). But how many minutes are there in two or more years? Well, it depends on how many of those are leap years with 366 days, per the Gregorian calendar, as some of them could have 1 x 24 x 60 = 1440
 additional minutes. In fact, how many minutes has it been since you were born? Well, that, too, depends on how many leap years there have been since! There is an algorithm for such, but let’s not reinvent that wheel. Let’s use a library instead. Fortunately, Python comes with a datetime module that has a class called date that can help, per docs.python.org/3/library/datetime.html#date-objects.

In a file called seasons.py, implement a program that prompts the user for their date of birth in YYYY-MM-DD format and then sings prints how old they are in minutes, rounded to the nearest integer, using English words instead of numerals, just like the song from Rent, without any and between words. Since a user might not know the time at which they were born, assume, for simplicity, that the user was born at midnight (i.e., 00:00:00) on that date. And assume that the current time is also midnight. In other words, even if the user runs the program at noon, assume that it’s actually midnight, on the same date. Use datetime.date.today to get today’s date, per docs.python.org/3/library/datetime.html#datetime.date.today.

Structure your program per the below, not only with a main function but also with one or more other functions as well:

from datetime import date


def main():
    ...


...


if __name__ == "__main__":
    main()

You’re welcome to import other (built-in) libraries, or any that are specified in the below hints. Exit via sys.exit if the user does not input a date in YYYY-MM-DD format. Ensure that your program will not raise any exceptions.

'''

from datetime import date
import inflect
import re
import sys

# Initialize inflect
p = inflect.engine()


def main():

    # Prompt user
    try:
        # After validating input through validate function, store results in variables
        year, month, day = validate(input("Date of Birth: "))
    # Exit with message if invalid
    except:
        sys.exit("Invalid input")

    # Convert results through convert function and print output
    date_out = convert(year, month, day)
    print(f"{date_out.capitalize()} minutes")


# Function to validate input is in format YYYY-MM-DD
def validate(date_in):

    # Searches for pattern and compares with input
    if re.search(r"^(\d{4})-(\d{2})-(\d{2})$", date_in):
        # Divides str into constituent parts amd returns result
        year, month, day = date_in.split('-')

        return year, month, day


# Function to calculate minutes from years and return in words
def convert(year, month, day):
    # Convert input strs to ints
    dob = date(int(year), int(month), int(day))
    # Get today's date
    todays_date = date.today()
    # Calculate amount of days since date of birth
    difference = todays_date - dob
    # Calculate that result in minutes
    mins = difference.days * 24 * 60
    # Convert to word removing 'and' and return result
    date_out = p.number_to_words(mins, andword='')

    return date_out


if __name__ == "__main__":
    main()