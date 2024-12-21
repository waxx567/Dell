# From: https://cs50.harvard.edu/python/2022/psets/5/test_fuel/

import sys

def main():
    while True:
        # Keep prompting user until a fraction is keyed
        try:
            fraction = input("Fraction: ")
            if len(fraction) == 3 and fraction[1] == '/':
                # Return value of convert function saved to variable
                percentage = convert(fraction)
                # That value as input to gauge function and output saved
                reading = gauge(percentage)
                # Print that value
                print(reading)
                sys.exit(0)
        except TypeError:
            print("TypeError")
            print("Usage: X/Y (where X < Y < 0)")
            sys.exit(1)
        except ValueError:
            print("ValueError")
            print("Usage: X/Y (where X < Y < 0)")
            sys.exit(1)
        except ZeroDivisionError:
            print("ZeroDivisionError")
            print("Usage: X/Y (where X < Y < 0)")
            sys.exit(1)

# Function to convert fraction to percentage
def convert(fraction):

        # Split fraction into constituent parts
        numer, denom = fraction.split("/")
        # Convert strings to integers
        numer, denom = int(numer), int(denom)
        # Express denominator as percentage of whole
        section = 100 / denom
        # Multiply that by nuerator and round answer
        percent = round(section * numer)
        # Return that value
        return percent

def gauge(percentage):

    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()