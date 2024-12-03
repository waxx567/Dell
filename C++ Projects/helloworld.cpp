#include <iostream>

/**
 * @brief Demonstrates the use of pointers in C++.
 *
 * @details This function initializes a string variable and a pointer 
 *          to that string, then prints the address stored in the pointer.
 *
 * @return 0 on successful execution.
 */
int main() {

    std::string name = "Wayne";
    std::string *namePtr = &name;

    // prints the value of the pointer
    std::cout << *namePtr << std::endl;

    return 0;
}