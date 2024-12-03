#include <iostream>

/**
 * @brief Entry point of the program
 *
 * This program demonstrates the use of null pointers and the nullptr keyword.
 * It checks if a pointer has been assigned a null value and prints the result to the console.
 *
 * @return 0 on success
 */
int main() {

    // null value = when a pointer is pointing at a null value
    //              that pointer is not pointing to anything
    // null pointer = a pointer that is not pointing to anything
    //                useful when determining if an address 
    //                was successfully assigned to a pointer
    // nullptr = keyword representing the null pointer literal

    int *p = nullptr;
    int x = 567;

    p = &x;

    // IF THE POINTER IS ASSIGNED, IT IS SAFE TO DEREFERENCE!

    if (p == nullptr) {
        std::cout << "p was not assigned" << std::endl;
    }
    else {
        std::cout << "p was assigned" << std::endl;
        std::cout << *p << std::endl;
    }
    
    return 0;
}