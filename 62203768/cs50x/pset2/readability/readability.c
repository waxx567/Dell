#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

// Declare global variables
int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{

    // Get user input
    string text = get_string("Text: ");

    // Call function that counts letters, input string and store total in letters variable
    int letters = count_letters(text);

    // Call function that counts words, input string and store total in words variable
    int words = count_words(text);

    // Call function that counts sentences, input string and store total in sentences variable
    int sentences = count_sentences(text);

    // Calculate number of letters per 100 words in the text
    float L = (float) letters / (float) words * 100;

    // Calculate number of sentences per 100 words in the text
    float S = (float) sentences / (float) words * 100;

    // Apply Coleman-Liau Index
    int grade = (0.0588 * L - 0.296 * S) - 15.8;

    // If Coleman-Liau Index is below 1
    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }

    // If Coleman-Liau Index is between 1 and 16
    else if (grade >= 1 && grade <= 16)
    {
        printf("Grade %i\n", grade);
    }

    // If Coleman-Liau Index is over 16
    else
    {
        printf("Grade 16+\n");
    }
}

// Function to count letters
int count_letters(string text)
{

    // Variable to store text length
    int i = strlen(text);

    // Variable to store letter count
    int letter_count = 0;

    // Loop through text until end, incrementing by one character with each iteration
    for (int j = 0; j < i; j++)
    {

        // If the current character is alphabetic or one of several other identified characters, add one to the letter count
        if (isalpha(text[j]) || (text[j] > 33 && text[j] < 63))
        {
            letter_count++;
        }
    }

    return letter_count;
}

// Function to count words
int count_words(string text)
{

    // Variable to store text length
    int i = strlen(text);

    // Variable to store word count
    int word_count = 0;

    // Loop through text until end, incrementing by one character with each iteration
    for (int j = 0; j < i; j++)
    {

        // If the current character is whitespace, add one to the word count
        if (text[j] == 32)
        {
            word_count++;
        }
    }

    // The final word will not end in a white space, add one for that
    word_count = word_count + 1;

    return word_count;
}

// Function to count sentences
int count_sentences(string text)
{
    // Variable to store text length
    int i = strlen(text);

    // Variable to store sentence count
    int sentence_count = 0;

    // Loop through text until end, incrementing by one character with each iteration
    for (int j = 0; j < i; j++)
    {

        // If current character is 33(!) or 46(.) or 63(?), add one to sentence count
        if (text[j] == 33 || text[j] == 46 || text[j] == 63)
        {
            sentence_count++;
        }
    }

    return sentence_count;
}