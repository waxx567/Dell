from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

"""Knowledge base"""
knowledge = And(
    Or(AKnight, AKnave),  # A is either a knight or a knave
    Not(And(AKnight, AKnave)),  # A cannot be a knight and a knave
    Or(BKnight, BKnave),  # B is either a knight or a knave
    Not(And(BKnight, BKnave)),  # B cannot be a knight and a knave
    Or(CKnight, CKnave),  # C is either a knight or a knave
    Not(And(CKnight, CKnave))  # C cannot be a knight and a knave
)

# Each character is either a knight or a knave. Every sentence spoken by a knight is true, and every sentence spoken by a knave is false.

# Puzzle 0
# A says "I am both a knight and a knave."
# A says (AKnight ^ AKnave)
# If AKnight => (AKnight ^ AKnave)
# If AKnave => ¬(AKnight ^ AKnave)
knowledge0 = And(
    knowledge,  # The main knowledge base tells the AI what rules are to be considered when parsing the statement
    Implication(AKnight, And(AKnight, AKnave)),  # If A is a knight then the statement is true
    Implication(AKnave, Not(And(AKnight, AKnave)))  # If A is a knave then the statement is false
)
# A is a Knave

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
# A says (AKnave ^ BKnave)
# If AKnight => (AKnave ^ BKnave)
# If AKnave => ¬(AKnave ^ BKnave)
knowledge1 = And(
    knowledge,  # The main knowledge base tells the AI what rules are to be considered when parsing the statement
    Implication(AKnight, And(AKnave, BKnave)),  # If A is a knight then the statement is true
    Implication(AKnave, Not(And(AKnave, BKnave)))  # If A is a knave then the statement is false
)
# A is a Knave
# B is a Knight

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
# A says (AKnight ^ BKnight) v (AKnave ^ BKnave)
# B says (AKnight ^ BKnave) v (AKnave ^ BKnight)
# If AKnight => (AKnight ^ BKnight) v (AKnave ^ BKnave)
# If AKnave => ¬(AKnight ^ BKnight) v ¬(AKnave ^ BKnave)
# If BKnight => (AKnight ^ BKnave) v (AKnave ^ BKnight)
# If BKnave => ¬(AKnight ^ BKnave) v ¬(AKnave ^ BKnight)
knowledge2 = And(
    knowledge,  # The main knowledge base tells the AI what rules are to be considered when parsing the statement
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),  # If A is a knight then his statement is true
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),  # If A is a knave then his statement is false
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),  # If B is a knight then his statement is true
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))))  # If B is a knave then his statement is false
)
# A is a Knave
# B is a Knight

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
# A says (AKnight v AKnave)
# B says A says (AKnave)
# B says (CKnave)
# C says (AKnight)
# If AKnight => (AKnight v AKnave)
# If AKnave => ¬(AKnight v AKnave)
# If BKnight =>
# If BKnave =>
# If BKnight => (CKnave)
# If BKnave => ¬(CKnave)
# If CKnight => (AKnight)
# If CKnave => ¬(AKnight)
knowledge3 = And(
    knowledge,  # The main knowledge base tells the AI what rules are to be considered when parsing the statement
    Implication(AKnight, Or(AKnight, AKnave)),  # If A is a knight then whatever he says is true
    Implication(AKnave, Not(Or(AKnight, AKnave))),  # If A is a knave then whatever he says is false
    Or(Implication(BKnight, Or(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave)))), Implication(
        BKnave, Not(Or(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave)))))),  # Parsing what B says that A says
    Implication(BKnight, CKnave),  # If B is a knight then whatever he says about C is true
    Implication(BKnave, Not(CKnave)),  # If B is a knave then whatever he says about C is false
    Implication(CKnight, AKnight),  # If C is a knight then whatever he says is true
    Implication(CKnave, Not(AKnight)),  # If C is a knave then whatever he says is false
)
# A is a Knight
# B is a Knave
# C is a Knight


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()