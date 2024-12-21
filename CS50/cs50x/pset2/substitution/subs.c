// A substitution cipher

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Declares function that validates user input
int validation(string s);

int main(int argc, string argv[])
{

    // Put user input into s variable
    string s = argv[1];

    // Variables containing all upper and lowercase letters
    string t = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    string u = "abcdefghijklmnopqrstuvwxyz";

    // User must input two arguments only
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    // Calls function that validates user input and puts return value in num variable
    int num = validation(s);

    // If NULL is returned
    if (num == 1)
    {
        return 1;
    }

    // Prompt user for input
    string p = get_string("plaintext:  ");

    // Lead in before encoded answer
    printf("ciphertext: ");

    // Declare variables outside loop
    int w;
    int x;
    int y;
    int z;

    // Loop through plaintext till end one character at a time
    for (int i = 0, n = strlen(p); i < n; i++)
    {

        // If the current character is not alphabetic, print it
        if (!isalpha(p[i]))
        {
            printf("%c", p[i]);
        }

        // If the current character is lowercase
        if (p[i] >= 97 && p[i] <= 122)
        {

            // Assign that character to w variable
            w = p[i];

            // Loop through the lowercase letter set one character at a time
            for (int j = 0, m = strlen(u); j < m; j++)
            {

                // When w matches one of the set, print the encryption letter
                if (w == u[j])
                {
                    x = w - 97;
                    printf("%c", tolower(s[x]));
                }
            }
        }

        // If the current character is uppercase
        if (p[i] >= 65 && p[i] <= 90)
        {

            // Assign that character to y variable
            y = p[i];

            // Loop through the uppercase letter set one character at a time
            for (int k = 0, o = strlen(t); k < o; k++)
            {

                // When y matches one of the set, print the encryption letter
                if (y == t[k])
                {
                    z = y - 65;
                    printf("%c", toupper(s[z]));
                }
            }
        }
    }

    // Go to a new line
    printf("\n");
}

// Function validates user input
int validation(string s)
{

    // Key must contain 26 characters
    if (strlen(s) != 26)
    {
        printf("Key must contain 26 characters\n");
        return 1;
    }

    // Loop through key
    for (int i = 0, n = strlen(s); i < n; i++)
    {

        // Only letters permitted
        if (!isalpha(s[i]))
        {
            printf("Key must have letters only\n");
            return 1;
        }

        // Otherwise they are all letters
        else
        {

            // Only unique letters permitted
            if (s[i] != '\0')
            {
                int count = 0;
                count++;
                if (count > 1)
                {
                    printf("Key may not contain duplicates\n");
                    return 1;
                }
            }

            // When end of string is reached and no duplicates have been found
            else if (s[i] == '\0')
            {
              return 0;
            }
        }
    }
    return 0;
}