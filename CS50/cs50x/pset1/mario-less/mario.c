// Used Libraries
#include <stdio.h>
#include <cs50.h>

// Prototype functions
int n();
void draw(int h);

// Simplest main loop ever
int main(void)
{
    int h = n();
    draw(h);
}

// Function to receive and check the required height value
int n()
{
    // Initializing a outside do Loop otherwise while won't get it
    int a;
    do
    {
        a = get_int("Height: ");
    }
    while (a < 1 || a > 8);

    // Return value of a to h
    return a;
}

// Function that draws the pyramid
void draw(int h)
{
    // Mother Loop, provides an increasing variable and breaks end of lines at each row
    for (int i = 0; i < h; i++)
    {
        // 1st Nested, prints spaces that make the pyramid face to the right side
        for (int spaces = i + 1; spaces < h; spaces++)
        {
            printf(" ");
        }

        // 2nd Nested, prints the actual pyramid
        for (int j = h + i + 1; j > h; j--)
        {
            printf("#");
        }
        printf("\n");
    }
}