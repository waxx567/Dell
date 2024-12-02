#include <iostream>

/**
 * @brief The main entry point of the program
 *
 * @details This function demonstrates how to print the memory address of a
 *          variable to the console.
 *
 * @return 0 on success
 */
int main() {

    // memory address = the location in memory where a variable is stored
    //                  address can be accessed using the & symbol

    std::string name = "Wayne";
    int age = 30;
    bool isMale = true;

    std::cout << "Address of name: " << &name << std::endl;
    std::cout << "Address of age: " << &age << std::endl;
    std::cout << "Address of isMale: " << &isMale << std::endl;

    return 0;
}