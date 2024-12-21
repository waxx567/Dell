# Introducing classes
# A class is kind of like a blueprint for pieces of data - objects, so to speak - a mould that you can define and give a name and when you use that blueprint, you get types of data that are designed exactly as you want
# Classes allow you to invent your own datatypes in Python and give them a name
class Student:
    ...


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student


if __name__ == "__main__":
    main()

# This works even though there is nothing in the Student class. Lines 4 and 5 are sufficient to create the class and every time you use that class, you create what are known as objects.
# That is what you are doing on line 14 ie. creating an object of that class. Using the metaphor of the mould again, the mould defines the shape and whatever you pour into the mould instantiates an object ie. an instance of the class
# Here it is mutable but we will see how to make instances immutable later
# name and house are attributes of the class, more technically known as instance variables