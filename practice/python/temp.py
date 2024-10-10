# Given a list of temperatures, return the one closest to zero whether positive or negative
import sys
import math


def main():
    # List of temperatres
    ts = [-14, 78, -25, 4, -10, 42, 11, -3, -45]
    # Call function plugging in list
    x = compute_closest_to_zero(ts)
    # Print answer
    print(f"x: {x}")


# Function returns which given temp is closest to zero
def compute_closest_to_zero(list):
    # Zero determines which is which
    less, more = 0, 0
    # Iterate through list
    for temp in list:
        # Assign value if following conditions are met
        if temp < 0:
            # If no negative values have been seen yet
            if less == 0:
                # This temp value stored in less
                less = temp
            else:
                # If less != 0 and temp is closer than less to zero
                if temp > less:
                    # This temp value stored in less
                    less = temp
        # If temp > 0
        else:
            # If no positive values have been seen yet
            if more == 0:
                # This temp value stored in more
                more = temp
            else:
                # If more != 0 and temp is closer than more to zero
                if temp < more:
                    # This temp value stored in more
                    more = temp
    # Variable stores positive value of less to plug into return statement
    i = 0 - less
    return less if i < more else more
    # Return less if the positive of less is less than more otherwise return more


if __name__ == "__main__":
    main()