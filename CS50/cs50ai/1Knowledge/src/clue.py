"""Knowledge Engineering"""

import termcolor

from logic import *

# Propositional Symbols
mustard = Symbol("ColMustard")
plum = Symbol("ProfPlum")
scarlet = Symbol("MsScarlet")
characters = [mustard, plum, scarlet]

ballroom = Symbol("ballroom")
kitchen = Symbol("kitchen")
library = Symbol("library")
rooms = [ballroom, kitchen, library]

knife = Symbol("knife")
revolver = Symbol("revolver")
wrench = Symbol("wrench")
weapons = [knife, revolver, wrench]

symbols = characters + rooms + weapons


# Function takes the knowledge base and draws conclusions based on it
def check_knowledge(knowledge):
    # Loop through all symbols
    for symbol in symbols:
        # Check if model is true and print conclusion if it is
        if model_check(knowledge, symbol):
            termcolor.cprint(f"{symbol}: YES", "green")
        # Check if model is not false and print conclusion if it is not
        elif not model_check(knowledge, Not(symbol)):
            print(f"{symbol}: MAYBE")


# Knowledge Base
# There must be one of each person, room, and weapon in the answer.
knowledge = And(
    Or(mustard, plum, scarlet),
    Or(ballroom, kitchen, library),
    Or(knife, revolver, wrench)
)

# print(knowledge.formula())

# python clue.py
# (ColMustard v ProfPlum v MsScarlet) ∧ (ballroom v kitchen v library) ∧ (knife v revolver v wrench))

# Add information from initial cards - the cards I started with - to the knowledge base
knowledge.add(And(
    Not(mustard), Not(kitchen), Not(revolver)
))

# Add additional information revealed - either scarlet or library or wrench cannot be true - to the knowledge base
knowledge.add(Or(
    Not(scarlet), Not(library), Not(wrench)
))

# Add other information - revealed as the game continues - to the knowledge base
knowledge.add(Not(plum))
knowledge.add(Not(ballroom))

check_knowledge(knowledge)

# python clue.py
# MsScarlet: YES
# library: YES
# knife: YES
# All printed in green as specified by cprint.