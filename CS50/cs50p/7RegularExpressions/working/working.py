'''
Whereas most countries use a 24-hour clock, the United States tends to use a 12-hour clock. Accordingly, instead of “09:00 to 17:00”, many Americans would say they work “9:00 AM to 5:00 PM” (or “9 AM to 5 PM”), wherein “AM” is an abbreviation for “ante meridiem” and “PM” is an abbreviation for “post meridiem”, wherein “meridiem” means midday (i.e., noon).

In a file called working.py, implement a function called convert that expects a str in either of the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each. Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

9:00 AM to 5:00 PM
9 AM to 5 PM

Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

Structure working.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.

import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    ...


...


if __name__ == "__main__":
    main()

'''

import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Search for time pattern
    format_ok = re.search(r"^(([0-9][0-2]*):*([0-5][0-9]*)* ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9]*)* ([A-P]M)))$", s)
    # If time pattern detected
    if format_ok:
        # Split elements
        parsed = format_ok.groups()
        # If either hour exceeds 12
        if int(parsed[1]) > 12 or int(parsed[5]) > 12:
            raise ValueError
        # Call function to format input using relevant parsed elements and return result to main
        time_one = format_input(parsed[1], parsed[2], parsed[3])
        time_two = format_input(parsed[5], parsed[6], parsed[7])
        return time_one + " to " + time_two
    # If time pattern is not found
    else:
        raise ValueError


# Function to format input correctly
def format_input(hour, minute, meridium):

    if meridium == "PM":
        if int(hour) == 12:
            format_hour = 12
        else:
            format_hour = int(hour) + 12
    else:
        if int(hour) == 12:
            format_hour = 0
        else:
            format_hour = int(hour)

    if minute == None:
        format_minute = ":00"
        format_time = f"{format_hour:02}" + format_minute
    else:
        format_time = f"{format_hour:02}" + ":" + minute

    return format_time


if __name__ == "__main__":
    main()