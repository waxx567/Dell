// CS50x 2023 Lecture 5 list.c version 2

// Terminal input:  ./node 1 2 3
// Terminal output: 3
//                  2
//                  1

// This code introduces linked lists where values are not necessarily stored contiguously
// Adding a new value is not as inefficient as no copying of the original array is needed

#include <stdio.h>
#include <stdlib.h>

// Define a node
// Declare the struct name at the start because the struct is being used recursively within the struct
typedef struct node
{
    int number;         // Stored value
    struct node *next;  // Pointer to the next stored value
}
node;                   // Name of the struct

int main(int argc, char *argv[])

{
    node * list = NULL; // Declare new node

    // Iterate over the command line argument
    for (int i = 1; i < argc; i++)  // Start at 1 as the first argument is the file name
    {
        //  Convert the input string to an integer and assign that value to a variable
        int number = atoi(argv[i]);

        // Allocate a node
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return 1;       // Exit with error code 1 if there is no memory available
        }

        n->number = number; // Place the number in the node
        n->next = NULL;     // Remove the node's second garbage value

        n->next = list;     // Prepend the new node to the existing list
        list = n;           // Point the existing list at the new node
    }

    node *ptr = list;       // Declare a pointer to point at the same location at which list is pointed

    while (ptr != NULL)     // Loop over the list array until ptr == NULL
    {
        printf("%i\n", ptr->number); // Print the number stored in the list array
        ptr = ptr->next;             // Point the pointer at the next node (will be NULL if it is the last node)
    }

    ptr = list; // Reset the node

    while (ptr != NULL) // Loop over the list array until ptr == NULL
    {
        node *next = ptr->next; // Declare a temporary pointer to point at the next node
        free(ptr);              // Free the original pointer
        ptr = next;             // Point the original pointer at the same location at which the temporary pointer is pointed
    }
}