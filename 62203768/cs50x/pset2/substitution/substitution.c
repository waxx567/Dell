// A substitution cipher

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{

    // If user does not input two arguments only in the command line
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    // If the second argument is not the correct length
    if (strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    // Assign second argument to inString variable
    string inString = argv[1];

    // Array of bools that corresponds to the alphabet to check inString against
    char key[26];

    // Array to mark letters for duplicate check
    bool seen[26];

    // Set each item inside bool array to false
    for (int i = 0; i < 26; i++)
    {
        seen[i] = false;
    }

    // Check if characters entered in the command line are alphabetic and not duplicated
    for (int i = 0; i < 26; i++)
    {
        // If the characters are alphabetic
        if (isalpha(inString[i]))
        {
            // If the current letter is uppercase
            if (isupper(inString[i]))
            {
                // If the letter has been seen already
                if (seen[inString[i] - 'A'] == true)
                {
                    // The letter is repeated
                    printf("Key must not contain duplicate letters.\n");
                    return 1;
                }

                // Otherwise the letter has not been seen already
                else
                {
                    // Mark as seen
                    seen[inString[i] - 'A'] = true;
                    // Set the key array to correspond
                    key[i] = inString[i] - 'A';
                }
            }

            // If the current letter is lowercase
            else
            {
                // If the letter has been seen already
                if (seen[inString[i] - 'a'] == true)
                {
                    // The letter is repeated
                    printf("Key must not contain duplicate letters.\n");
                    return 1;
                }

                // Otherwise the letter has not been seen already
                else
                {
                    // Mark as seen
                    seen[inString[i] - 'a'] = true;
                    // Set the key array to correspond
                    key[i] = inString[i] - 'a';
                }
            }
        }
        // If the characters are not all alphabetic
        else
        {
            printf("Key must contain only letters.\n");
            return 1;
        }
    }

    // Prompt user for input text and store in plain variable
    string plain = get_string("plaintext: ");

    // Copy string to keep order while looping through original string
    string copy = plain;

    // Loop through input text
    for (int i = 0; i < strlen(plain); i++)
    {
        // If the current character is a letter
        if (isalpha(plain[i]))
        {
            // If the letter is uppercase
            if (isupper(plain[i]))
            {
                // Copy transformed letter mapped with key to copy
                copy[i] = (key[plain[i] - 'A'] + 'A');
            }

            // Otherwise the letter is lowercase
            else
            {
                // Copy transformed letter mapped with key to copy
                copy[i] = (key[plain[i] - 'a'] + 'a');
            }
        }

        // Otherwise current character is not a letter
        else
        {
            // Copy to copy as is
            copy[i] = plain[i];
        }
    }

    // Encoded answer
    printf("ciphertext: %s\n", copy);

    return 0;
}