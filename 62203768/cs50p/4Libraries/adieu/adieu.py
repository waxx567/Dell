# In The Sound of Music, there’s a song sung largely in English, So Long, Farewell, with these lyrics, wherein “adieu” means “goodbye” in French:

#     Adieu, adieu, to yieu and yieu and yieu

# Of course, the line isn’t grammatically correct, since it would typically be written (with an Oxford comma) as:

#     Adieu, adieu, to yieu, yieu, and yieu

# To be fair, “yieu” isn’t even a word; it just rhymes with “you”!

# In a file called adieu.py, implement a program that prompts the user for inStrings, one per line, until the user inputs control-d. Assume that the user will input at least one inString. Then bid adieu to those inStrings, separating two inStrings with one and, three inStrings with two commas and one and, and
# inStrings with

# commas and one and, as in the below:

#     Adieu, adieu, to Liesl
#     Adieu, adieu, to Liesl and Friedrich
#     Adieu, adieu, to Liesl, Friedrich, and Louisa
#     Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
#     Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
#     Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
#     Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl

import inflect

# initiate engine
inflectEngine = inflect.engine()

# list to store inputs
greetString = []

while True:
    try:
        # prompt user and add input/s to end of list
        inString = input("Name: ")
        greetString.append(inString)
    # incorrect input
    except EOFError:
        print()
        break

# use library (engine) to add inflections to list items
# and join them together
outString = inflectEngine.join(greetString)
# add prefix and output answer
print(f"Adieu, adieu, to {outString}")