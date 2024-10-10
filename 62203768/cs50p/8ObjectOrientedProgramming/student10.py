# Introducing methods - begins at 39:30 in Lecture 8
# The previous iteration is a little reckless as lines 14 and 15 allow the user to put ANY datatype inside of this student object
# We can standardize what those objects can be and what kinds of values you can set them to
class Student:
    # We define an instance method (dunder init in this case)
    def __init__(self, name, house):
        self.name = name
        self.house = house
        # This is a manifestation of Object-oriented Programming
        # self gives you access to the current object that has just been created


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    # Here we are treating the name of the class (Student) as a function and passing in two values (name and house)
    # Student(name, house) is known as a constructor call as it will construct (or instantiate) a Student object for me
    # It will use the Student class as a template (a mould, if you will) so that every Student is structured the same while still able to hold different information - Harry or Padma, Gryffindor or Ravenclaw
    # So the function that is always going to be called when you call the class is __init__() which implements the initialization of the object in Python
    return student


if __name__ == "__main__":
    main()

# This allows us to error check inputs