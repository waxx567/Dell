# We can define multiple classes that somehow relate to one another
# They don't need to exist sort of in parallelin this way
# There can be a hierarchy that allows inheritance of attributes
# Both students and professors are wizards
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    ...


# Adding the condition in parentheses after the class name signifies that this class (subclass) inherits from the Wizard class (superclass)
# super().__init__(name) inherits the name from the __init__ method
class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

    ...


# Adding the condition in parentheses after the class name signifies that this class (subclass) inherits from the Wizard class (superclass)
# super().__init__(name) inherits the name from the __init__ method
class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    ...