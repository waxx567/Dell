def incorrect_first_name():
    """
    Keep asking for the student's first name until a valid input is given.
    """

    while firstName.isalpha() == False:
        firstName = input("Enter the student's first name: ")  

def incorrect_last_name():
    """
    Keep asking for the student's last name until a valid input is given.
    """

    while lastName.isalpha() == False:
        lastName = input("Enter the student's last name: ")  

def choice():
    """
    Prompt the user to enter a student's first and last name, and
    return a string with the full name. The function will keep asking
    for the names until valid input (only letters) is given.
    """
    
    firstName = input("Enter the student's first name: ")
    incorrect_first_name()
    lastName = input("Enter the student's last name: ")
    incorrect_last_name() 
    student = firstName + " " + lastName

    return student


def main():
    """
    The main function. Present the user with a menu of options to
    add, remove, search for, list or quit. The function will keep
    running until the user chooses to quit.
    """

    studentList = []

    choice = 0

    while choice != 5:
        print("** Students **")
        print("Please choose an option:")
        print("1. Add a student")
        print("2. Remove a student")
        print("3. Search for a student")
        print("4. List all students")
        print("5. Quit")

        while choice < 1 or choice > 5:
            try:
                choice = int(input())
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")

        if choice == 1:
            student = choice()
            studentList.append(student)
            print("Student added.")
        elif choice == 2:
            student = choice()
            studentList.remove(student)
            print("Student removed.")
        elif choice == 3:
            student = choice()
            if student in studentList:
                print("Student found.")
            else:
                print("Student not found.")
        elif choice == 4:
            for student in studentList:
                print(student)
        elif choice == 5:
            print("Goodbye!")


if __name__ == "__main__":
    main()