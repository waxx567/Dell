// CS50x 2023 Lecture 5 introduces trees
// Big O of n

// Define node with two pointers
typedef struct node
{
    int number;         // Stored value
    struct node *left;  // Pointer to stored values to left of tree
    struct node *right; // Pointer to stored values to right of tree
}
node;                   // Name of struct

// Function to compare an input number to numbers in a tree returns a bool value
// Inputs a pointer to the tree and a number to search for
bool search(node *tree, int number)
{
    // The loop over the tree does a safety check first in case the tree is empty
    // This also ends the search as the last tree->next will be NULL
    if (tree == NULL)
    {
        return false;
    }
    else if (number < tree->number)
    {
        // The search number is less than the number at the location the pointer indicates
        // Go to the pointer indicating the left side of the tree
        // Check the input number against the number at the location the pointer indicates
        return(search(tree-left, number))
    }
    else if (number > tree->number)
    {
        // The search number is greater than the number at the location the pointer indicates
        // Go to the pointer indicating the right side of the tree
        // Check the input number against the number at the location the pointer indicates
        return(search(tree->right, number))
    }
    else
    {
        // The number matches
        return true;
    }
}