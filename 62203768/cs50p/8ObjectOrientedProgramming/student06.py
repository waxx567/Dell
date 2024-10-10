# The problem with the previous iteration of the code is that one has to remember the position of the data as in student[0] or student[1] - easy here as there are only two elements, but more difficult with many elements
# Let's try a different datatype - a dictionary
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")


def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student
    # Still returning one value (student) even though it has the two elements we need (the actual name and house) and is actually FOUR elements - two sets of key:value pairs (eg. name: Harry and house: Gryffindor)


if __name__ == "__main__":
    main()
