import random


class Hat():
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):
        print(name, "is in", random.choice(self.houses))

# We don't want to instantiate a sorting hat like this
# hat = Hat()
# because of the problem shown in hat2.py so
# go to hat4.py
hat.sort("Harry")