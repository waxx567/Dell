// CS50x 2023 Lecture 5 introduces tries for more complicated trees

// Define node as a linked list
typedef struct node
{
    char *number;               // Stored value
    struct node *children[26];  // Pointer to next stored value in an array of 26 nodes
}
node;                           // Name of struct

node trie;                      // Declare the node