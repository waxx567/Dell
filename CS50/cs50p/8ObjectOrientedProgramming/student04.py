# Tuples are immutable so the values cannot be changed after they have been returned from the function
# In this case, if a user types Padma for name and Gryffindor for house, a TypeError will be raised saying 'tuple does not support item assignment'
# meaning the datatype will not allow the action
def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
        # In the movies, she's in Gryffindor whereas she's in Ravenclaw in the books
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)


if __name__ == "__main__":
    main()
