// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Declare word counter variable
unsigned int count = 0;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    // Variable to store hashed word
    int hashnumber = hash(word);
    // Pointer to loop over the dictionary
    node *ptr = table[hashnumber];
    // Loop over the dictionary
    while (ptr != NULL)
    {
        // If the words are the same
        if (strcasecmp(ptr->word, word) == 0)
        {
            return true;
        }
        // Move to the next node
        ptr = ptr->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads the dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    // Open the dictionary
    FILE *infile = fopen(dictionary, "r");
    if (infile == NULL)
    {
        return false;
    }

    // Read strings from the dictionary one at a time
    // Variable to store each word including the string terminating character
    char inword[LENGTH + 1];

    // Loop over dictionary inspecting every word until the end of the file
    while (fscanf(infile, "%s", inword) != EOF)
    {
        // Create a new node for each word
        node *tmp = malloc(sizeof(node));
        if (tmp == NULL)
        {
            return false;
        }

        // Copy word into node
        strcpy(tmp->word, inword);

        // Hash word to obtain a hash value
        int hashnumber = hash(inword);

        // If the hash table is empty, this node becomes the only node in the linked list
        if (table[hashnumber] == NULL)
        {
            tmp->next = NULL;
        }

        // Otherwise, point this node's next field at the first node of the linked list
        else
        {
            tmp->next = table[hashnumber];
        }

        // Insert the node into the hash table at that location
        table[hashnumber] = tmp;

        // Increment word count
        count += 1;
    }
    fclose(infile);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return count;
}

// Function to free the node
void freenode(node *n)
{
    // If this is not the last node
    if (n->next != NULL)
    {
        // Call this function on the next node recursively
        freenode(n->next);
    }
    // Otherwise free the node
    free(n);
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    // Loop over every letter in the hash table
    for (int i = 0; i < N; i++)
    {
        // If the dictionary is not empty
        if (table[i] != NULL)
        {
            // Call the function to free the node
            freenode(table[i]);
        }
    }
    // Once all memory has been freed
    return true;
}