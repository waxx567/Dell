// Prints two mirrored pyramids
#include <cs50.h>
#include <stdio.h>

// Calls function
int get_input(void);

int main(void)
{

    int x = get_input();

    // For each row
    for (int i = 0; i < x; i++)
    {
        // For each space
        for (int k = x - i - 1; k > 0; k--)
        {
            // Print a space
            printf(" ");
        }
        // For each column
        for (int j = 0; j <= i; j++)
        {
            // Print a brick
            printf("#");
        }

        // Print two spaces between pyramids
        printf("  ");

        // Print right side
        for (int l = -1; l < i; l++)
        {
            printf("#");
        }

        // Move to next row
        printf("\n");
    }
}

// Function ensures user input within range
int get_input(void)
{
    int h;
    do
    {
        h = get_int("Height: ");
    }
    while (h < 1 || h > 8);
    return h;
}