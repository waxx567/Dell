# Executes the same code as speller problem from pset6 in Python
# A set is a collection of values with no duplicates
words =  set()
# This action gives you a hash table

def check(word):
    if word.lower() in words:
        return True
    else:
        return False

def load(dictionary):
    file = open(dictionary, "r")
    for line in file:
        word = line.rstrip()    # Removes newline char
        words.add(word)
    file.close()
    return True

def size():
    return len(words)

def unload():
    return True

# Far less code than speller.c but the trade-off is run time
# C program runs for 1.68 seconds, Python for 2.44 seconds