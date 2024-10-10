#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{

    // If user does not put two arguments only
    if (argc != 2)
    {
        printf("Incorrect command-line argument\n");
        return 1;
    }

    // If the second argument is not a number
    for (int i = 0, n = strlen(argv[1]); i < n; i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    // Converts the second argument from a string to an integer
    int c = atoi(argv[1]);

    // Variables declared globally
    int x;
    int y;

    // If user has input a negative integer
    if (c <= 0)
    {
        printf("Key must be a positive integer\n");
        return 1;
    }

    // Ensures the cipher still works with numbers greater than the alphabet range
    if (c > 26)
    {
        c = c % 26;
    }

    // Prompts user for message
    string s = get_string("plaintext:  ");

    // Lead in
    printf("ciphertext: ");

    // Loops through plaintext one character at a time
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        // If the current character is not alphabetic, print it
        if (!isalpha(s[i]))
        {
            printf("%c", s[i]);
        }

        // If the current character is lowercase
        if (s[i] >= 97 && s[i] <= 122)
        {

            // Assign the character to x and add the calculated amount
            x = s[i];
            x = x + c;

            // If x is out of upper bound
            if (x > 122)
            {

                // Bring x into range and print the result
                x = x - 26;
                printf("%c", x);
            }

            // Otherwise x is in range, print it
            else
            {
                printf("%c", x);
            }
        }

        // If the current character is uppercase
        if (s[i] >= 65 && s[i] <= 90)
        {

            // Assign the character to y and add the calculated amount
            y = s[i];
            y = y + c;

            // If y is out of upper bound
            if (y > 90)
            {

                // Bring y into range and print the result
                y = y - 26;
                printf("%c", y);
            }

            // Otherwise y is in range, print it
            else
            {
                printf("%c", y);
            }
        }
    }

    // Go to a new line before exiting
    printf("\n");
}