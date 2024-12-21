// CS50x 2023 Lecture 5 introduces tables for more complicated trees
// Big O of 1 but the trade-off is it uses a huge amount of memory

// Define node with two stored values
typedef struct node
{
    char *name;         // Stored value
    char *number;       // Stored value
    struct node *next;  // Pointer to next stored value
}
node;                   // Name of struct

// Declare a table of 26 nodes that are initially 26 NULL value empty buckets
node *table[26];