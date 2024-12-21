# We simplify the file by getting rid of properties to focus on an opportunity to clean up the code
# We want everything related to students to be in the Student class, especially for longer files
# Nobody wants to search through the file for other student related code
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
        # The line above means create an object of the current class (Student in this case)
    # Using @classmethod means we can call this get method without instantiating a Student object first


def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()

