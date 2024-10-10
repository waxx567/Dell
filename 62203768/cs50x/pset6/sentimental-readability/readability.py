# TODO

import cs50


def main():
    # Get string from user
    text = cs50.get_string("Text: ")
    # Call functions
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    # Calculate number of letters per 100 words in the text
    L = letters / words * 100
    # Calculate number of sentences per 100 words in the text
    S = sentences / words * 100

    # Apply Coleman-Liau Index
    grade = (0.0588 * L - 0.296 * S) - 15.8

    # Print grades
    if grade < 1:
        print("Before Grade 1")
    elif grade >= 1 and grade <= 16:
        print(f"Grade {round(grade)}")
    else:
        print("Grade 16+")


# Function to count letters
def count_letters(text):
    letter_count = 0
    for i in text:
        # If i is alphabetical
        if (i >= "A" and i <= "Z") or (i >= "a" and i <= "z"):
            letter_count += 1
    # Print statement used to check function is working
    # print(f"{letter_count} letters")
    return letter_count


# Function to count words
def count_words(text):
    word_count = 0
    for i in text:
        # Space denotes end of word
        if i == " ":
            word_count += 1
    # Final word does not end in a space so add one for that
    word_count += 1
    # Print statement used to check function is working
    # print(f"{word_count} words")
    return word_count


# Function to count sentences
def count_sentences(text):
    sentence_count = 0
    for i in text:
        # These symbols denote the end of a sentence
        if i in [".", "!", "?"]:
            sentence_count += 1
    # Print statement used to check function is working
    # print(f"{sentence_count} sentences")
    return sentence_count


main()