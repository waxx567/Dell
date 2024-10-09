"""Knowledge Engineering"""
# Logic Puzzles

# Gilderoy, Pomona, Minerva and Horace each belong to a different one of the four houses: Gryffindor, Hufflepuff, Ravenclaw and Slytherin House
# Gilderoy belongs to Gryffindor or Ravenclaw (GilderoyGryffindor V GilderoyRavenclaw)
# Pomona does not belong in Slytherin (¬PomonaSlytherin)
# Minerva belongs to Gryffindor (MinervaGryffindor)
# So MinervaGryffindor implies not MinervaRavenclaw (MinervaGryffindor => ¬MinervaRavenclaw), GilderoyRavenclaw implies not MinervaRavenclaw (GilderoyRavenclaw => ¬MinervaRavenclaw) and so on
# This is known for all people and all combinations of houses ie. every person/house combination (16 in total) is either true or false

from logic import *

people = ["Gilderoy", "Pomona", "Minerva", "Horace"]
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

symbols = []

knowledge = And()

# Create a symbol for each person/house combination
for person in people:
    for house in houses:
        symbols.append(Symbol(f"{person}{house}"))

# Each person belongs to a house
for person in people:
    knowledge.add(Or(
        Symbol(f"{person}Gryffindor"),
        Symbol(f"{person}Hufflepuff"),
        Symbol(f"{person}Ravenclaw"),
        Symbol(f"{person}Slytherin")
    ))

# Only one house per person
for person in people:
    for h1 in houses:
        for h2 in houses:
            if h1 != h2:
                knowledge.add(
                    Implication(Symbol(f"{person}{h1}"), Not(Symbol(f"{person}{h2}")))
                )

# Only one person per house
for house in houses:
    for p1 in people:
        for p2 in people:
            if p1 != p2:
                knowledge.add(
                    Implication(Symbol(f"{p1}{house}"), Not(Symbol(f"{p2}{house}")))
                )

# print(knowledge.formula())
# python puzzle.py
# Will show the knowledge base as stipulated above - a lot of info.

# Knowledge given:
knowledge.add(
    Or(Symbol("GilderoyGryffindor"), Symbol("GilderoyRavenclaw")) # Gilderoy is in Gryffindor or Ravenclaw.
)

knowledge.add(
    Not(Symbol("PomonaSlytherin")) # Pomona is not in Slytherin.
)

knowledge.add(
    Symbol("MinervaGryffindor") # Minerva is in Gryffindor.
)

for symbol in symbols:
    if model_check(knowledge, symbol):
        print(symbol)

# python puzzle.py
# GilderoyRavenclaw
# PomonaHufflePuff
# MinervaGryffindor
# HoraceSlytherin
