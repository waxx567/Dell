# An alternative to the previous iteration
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}
    # The other way was one line longer but perhaps more readable
    # This way is probably better in this instance as it is short, probably not so if the dictionary gets a lot more information


if __name__ == "__main__":
    main()
