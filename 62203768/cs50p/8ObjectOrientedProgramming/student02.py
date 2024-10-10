# get_name() and get_house() is fine but it would be cleaner to define a function called get_student() and let that do all of the work
# Returns the two values as a tuple
# A tuple is actually returning ONE value - the tuple - inside of which are two elements ie. the two values we want
# This can be written as
# return name, house
# but
# return (name, house)
# is more explicit and clearer to the reader
def main():
    name, house = get_student()
    print(f"{name} from {house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    # Now we want to return TWO values from our function as ONE student
    # One way is returning a dictionary but that's complicated
    # Python allows you to return two values as in:
    return name, house
    # But how do we access them?
    # Back to main


if __name__ == "__main__":
    main()
