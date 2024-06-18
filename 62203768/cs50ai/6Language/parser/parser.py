import nltk
import sys

# Set of context-free grammar rules for generating terminal symbols
TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

# Set of context-free grammar rules for generating nonterminal symbols
NONTERMINALS = """
S -> NP V | NP VP Conj VP | NP VP Conj NP VP

AP -> Adj | AP Adj
NP -> N | Det N | Det AP N | NP P NP | P NP
VP -> V | V Adv | Adv VP | VP NP | V NP Adv
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    # Nltk tokenizer requires punkt package
    # Download if not downloaded or not up-to-date
    nltk.download("punkt")

    # Empty list to store words
    words = []
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    # Loop over words in sentence
    for word in sentence:
        # Loop over characters in words
        for char in word:
            # If there is at least one alphabetic charcter in the word
            if char in chars:
                # Append the word's token to the words list  
                words.append(nltk.word_tokenize(word))

    return words

def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    '''
    # Empty list for chunks
    chunks = []

    # Convert the input tree to a parent tree
    parent = nltk.tree.ParentedTree.convert(tree)

    # Loop over subtrees in the parent tree
    for subtree in parent.subtrees():
        # If the subtree label is N, then the parent chunk label will be NP
        if subtree.label() == 'N':
            # Append the parent to the chunks list
            chunks.append(subtree.parent())
    '''
    return NotImplementedError

if __name__ == "__main__":
    main()
