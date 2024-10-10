def main():
    student = get_student()
    # List or tuple
    '''if student[0] == "Padma":
        student[1] == "Ravenclaw"
    print(f"{student[0]} from {student[1]}")'''
    # Dict
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")


def get_student():
    name = input("Name:  ")
    house = input("House: ")
    # Returning mutable list or immutable tuple
    '''return [name, house]    # If you want the return values in a list
    #return (name, house)   # For an immutable tuple'''
    # Returning dictionary
    '''student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student'''
    # Or
    return {"name": name, "house": house}


if __name__ == "__main__":
    main()