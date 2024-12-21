# Introducing properties and decorators
# A property is an attribute that has more defense mechanisms in place
# Decorators are functions that modify the behaviour of other functions
# We want to prevent the addition of something like `student.house = "Number Four, Privet Drive"` from being able to introduce a bug into the program
# Let's require that in order to access (get) some attribute, you go though some function
# and let's also require that in order to set some attribute, you go though some function
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter
    # A getter is a function in some class that gets some attribute
    @property
    def house(self):
        return self._house

    # Setter
    # A setter is a function in some class that sets some value
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house
        # The underscore is there because the instance variables and the function have the same name (house) and Python needs to be shown how to differentiate between the two when it stores the value
        # So now the instance variable is called _house and the property is called house


def main():
    student = get_student()
    # Running python student18.py and including the following line
    # student.house = "Number Four, Privet Drive"
    # will raise our ValueError: Invalid house
    # which will still also happen if the user inputs incorrect house information
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()

