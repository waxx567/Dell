# In the world of Harry Potter, there is only ONE sorting hat though
import random


class Hat():
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):
        print(name, "is in", random.choice(self.houses))


hat = Hat()
# We don't want there to be more than one hat as in
# hat1 = Hat()
# hat2 = Hat()
# so go to
# hat3.py
hat.sort("Harry")