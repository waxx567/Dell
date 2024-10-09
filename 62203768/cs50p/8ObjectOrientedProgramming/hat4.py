# Introducing @classmethod
# Up until now we have been using instance methods - writing functions inside of classes that are automatically passed a reference to self, the current object
# but sometimes we just don't need that
# Sometimes it suffices to just know what the class is and assume that there might not even be any objects of that class so
# in this sense, you can use a class really as a container for data and/or functionality that is just somehow conceptually related
# @classmethod allows us to do just this
import random


class Hat():
    # If we're not going to instantiate multiple houses as per the previous iteration, we don't need the __init__ method because that is really meant to initialize specific objects from that blueprint, that mould:
    # def __init__(self):
        # and if that goes, there is no self so the next line
        # self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
        # becomes
    # and indents to where the def __init__ was (obviously)
    # So in addition to class methods (functions), there are also class variables, which exist within the class itself and there is just one copy of that variable for all of the objects thereof as in:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    # With sort, it doesn't really make sense to within a specific sorting hat because we only want there to be one so we can specify that this is a classmethod
    @classmethod
    # and no longer pass in self but rather a reference to the class itself
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

# Now we don't have to instantiate any Hat objects (hat = Hat()), we just access the classmethod inside the Hat class
# using name of class dot method name passing in any arguments we want
Hat.sort("Harry")