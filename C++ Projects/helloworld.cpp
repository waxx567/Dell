#include <iostream>

/**
 * @brief The main entry point of the program
 *
 * @details This function demonstrates the use of dynamic memory allocation in C++.
 *          It allocates memory on the heap using the 'new' keyword, assigns a value
 *          to the memory, prints the address and value of the memory, and then
 *          deallocates the memory using the 'delete' keyword.
 *
 * @return 0 on successful execution
 */
int main() {

    // dynamic memory allocation = the process of creating memory on the heap
    // whenever you use the 'new' operator, you should also use the 'delete' operator
    //                           = memory that is allocated after the program is compiled and running
    // Use the 'new' keyword to allocate memory on the heap
    // Use the 'delete' keyword to deallocate memory on the heap
    // Useful when we don't know how much memory we need
    // Program is more flexible and can be more memory efficient
    // especially when handling user input or large datasets

    // declare an unassigned pointer
    int *p = NULL;  // this is a null pointer

    // is NULL the same as nullptr in C++?

    // in general yes, both assign the null value to pointer-like types

    // It doesn't convert to numeric values in either language. One difference though is that in C++ nullptr can convert to bool. This is not true in C#.

    // allocate memory on the heap
    p = new int;    // this is a pointer to an integer

    // assign a value to the memory
    *p = 42;

    // print the address of the memory
    std::cout << "The address of the memory is: " << p << std::endl;

    // print the value of the memory
    std::cout << "The value of the memory is: " << *p << std::endl;

    // deallocate memory on the heap
    delete p;

    // FAILURE TO FREE THE MEMORY CAN CAUSE A MEMORY LEAK

    return 0;
}