# So tuples are useful if the datatype will not change, and using a tuple is a secure way to ensure the values cannot be changed
# If you want the ability to change information, a different datatype will have to be used.
def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    # Square brackets means returning a list, which is mutable
    return [name, house]
    #  Now typing Padma for name and Gryffindor for house returns Padma from Ravenclaw


if __name__ == "__main__":
    main()
