def main():

    """
    Runs the main menu for the student records program.

    The menu provides options to add a student, view all students, delete a student, or quit the program.
    """
    
    studentList = []

    choice = 0

    while choice != 4:
        print("1. Add student")
        print("2. View all students")
        print("3. Delete student")
        print("4. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            firstName = input("Enter student's first name: ")
            lastName = input("Enter student's last name: ")
            course = input("Enter student's course: ")
            student = {"firstName": firstName, "lastName": lastName, "course": course}
            studentList.append(student)  
        elif choice == 2:
            for student in studentList:
                print(f"{student['firstName']} {student['lastName']} - {student['course']}")
        elif choice == 3:
            firstName = input("Enter student's first name: ")
            lastName = input("Enter student's last name: ")
            for student in studentList:
                if student["firstName"] == firstName and student["lastName"] == lastName:
                    studentList.remove(student)
                    print(f"{firstName} {lastName} deleted")
                    break
                else:
                    print(f"{firstName} {lastName} not found")
        elif choice == 4:
            print("Goodbye")
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()