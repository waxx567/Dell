from logic import *

rain = Symbol("rain") # It is raining
hagrid = Symbol("hagrid") # Harry visited Hagrid
dumbledore = Symbol("dumbledore") # Harry visited Dumbledore

"""Knowledge base"""
knowledge = And(
    Implication(Not(rain), hagrid), # If it is not raining, Harry visited Hagrid
    Or(hagrid, dumbledore), # Harry visited either Hagrid or Dumbledore
    Not(And(hagrid, dumbledore)), # Harry did not visit both Hagrid and Dumbledore
    dumbledore # Harry did visit Dumbledore
)

# print(knowledge.formula())

# python harry.py
# ((¬rain) => hagrid) ∧ (hagrid v dumbledore) ∧ (¬(hagrid ∧ dumbledore)) ∧ dumbledore

# This formula represents a logical representation of the information the computer is using to represent the knowledge base.

# Check the model to answer the query: Based on this information, is it raining?
print(model_check(knowledge, rain))

# python harry.py
# True
# It is raining.