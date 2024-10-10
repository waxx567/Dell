// CS50x 2023 Lecture 5

// Terminal input:  ./list 1 2 3
// Terminal output: 1
//                  2
//                  3

// This code shows the steps necessary to add an integer to a list without leaking memory
// The problem is that the complete array must be copied to a new one every time a new value is added

#include <stdio.h>
#include <stdlib.h>

int main(void)

{
    // Allocate pointer to array of chunk of memory - exit if no memory available
    int *list = malloc(3 * sizeof(int));
    if (list == NULL)
    {
        return 1;
    }

    // Populate array
    list[0] = 1;
    list[1] = 2;
    list[2] = 3;

    // Reallocate original pointer to temporary array of chunk of memory - exit if no memory available
    int *tmp = realloc(list, 4 * sizeof(int));
    if (tmp == NULL)
    {
        free(list); // Memory must be freed before exiting
        return 1;
    }

    list = tmp;  // Point original pointer at temporary array
    list[3] = 4; // Add new value to that array

    for (int i = 0; i < 3; i++)
    {
        printf("%i\n", list[i]);
    }

    free(list); // Memory must be freed before exiting
    return 0;
}