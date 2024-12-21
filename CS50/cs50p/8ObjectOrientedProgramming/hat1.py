# Let's add a list of houses for whenever a Hat object is instantiated
import random


class Hat():
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):
        # house = random.choice(self.houses)
        # print(name, "is in", house)
        # Tighten the above to one line as in
        print(name, "is in", random.choice(self.houses))


hat = Hat()
hat.sort("Harry")