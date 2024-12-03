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
    int age = 30;

    std::string *namePtr = &name;
    int *agePtr = &age;

    // prints the value at the address
    std::cout << *namePtr << std::endl;
    std::cout << *agePtr << std::endl;

    return 0;
}