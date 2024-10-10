class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        # If you were to add the underscore here
        self._house = house
        # there would be no error checking at all, so don't do it

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()

