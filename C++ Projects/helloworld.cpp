#include <iostream>

/**
 * @brief Main function of the program
 *
 * This function initializes a string 'name', a double 'pi', a char 'grade',
 * and a bool 'hungry'. It then outputs the size in bytes of the 'hungry' 
 * boolean variable to the console.
 *
 * @return 0 on success
 */
int main() {

    std::string name = "John";
    double pi = 3.14159;
    char grade = 'A';
    bool hungry = true;

    std::cout << sizeof(hungry) << " bytes" << std::endl;

    return 0;
}