# The previous iteration without the comments
import random


class Hat():
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")

# This is a very simple case that could be rendered simply as shown in hat6.py for this specific case
# This is a demonstration to introduce a different way of modeling the world - it is not really compelling in this simple example but as our code gets longer, as we start collaborating with other people, as the problems we're trying to solve get more sophisticated, the code gets messy quickly
# This shows us how to organise our code better
#  In the world of Harry Potter, we can have a class for Student, a class for Professor, a class for the sorting Hat, etc
# OOP is a way of encapsulating related data ie. variables, related functionality ie. methods inside of things that have names
# These things are called classes