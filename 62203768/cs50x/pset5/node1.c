// CS50x 2023 Lecture 5 list.c version 3

// Alternate code to node.c explained in CAPS below

#include <stdio.h>
#include <stdlib.h>

// Define node
typedef struct node
{
    int number;         // Stored value
    struct node *next;  // Pointer to next stored value
}
node;                   // Name of struct

int main(int argc, char *argv[])

{
    node * list = NULL; // Declare new node - start a linked list

    // Iterate over command line argument - start at 1 as 1st argument is file name
    for (int i = 1; i < argc; i++)
    {
        //  Convert input string to integer and assign to variable
        int number = atoi(argv[i]);

        // Allocate node - exit with error code 1 if no memory available
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return 1;
        }

        n->number = number; // Place number in node
        n->next = NULL;     // Remove node's second garbage value

        n->next = list;     // Prepend new node to existing list
        list = n;           // Point existing list at new node
    }

    // THESE TWO LINES OF CODE BELOW
    // node *ptr = list; // Declare pointer to point at same location list is pointed
    // while (ptr != NULL) // Loop until ptr == NULL
    // REPLACED BY THE NEXT ONE
    while (node *ptr = list; ptr != NULL; ptr++)
    {
        printf("%i\n", ptr->number); // Print last number stored in list
        ptr = ptr->next;             // Point pointer at next node (or NULL if last)
    }

    ptr = list; // Reset the node

    while (ptr != NULL) // Loop until ptr == NULL
    {
        node *next = ptr->next; // Declare temporary pointer to point at next node
        free(ptr);              // Free original pointer
        ptr = next;             // Original pointer to point at same location temporary pointer is pointed
    }
}