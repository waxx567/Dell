#include <iostream>

/**
 * @brief Main function of the program
 *
 * This function initializes a string 'name' and a double 'pi'. It then 
 * outputs the size in bytes of the 'name' string to the console.
 *
 * @return 0 on success
 */
int main() {

    std::string name = "John";
    double pi = 3.14159;

    std::cout << sizeof(name) << " bytes" << std::endl;

    return 0;
}