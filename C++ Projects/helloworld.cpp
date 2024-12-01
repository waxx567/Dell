#include <iostream>

/**
 * @brief Main function of the program
 *
 * This function initializes a string 'name', a double 'pi', and a char 'grade',
 * and outputs the size in bytes of the 'grade' char to the console.
 *
 * @return 0 on success
 */
int main() {

    std::string name = "John";
    double pi = 3.14159;
    char grade = 'A';

    std::cout << sizeof(grade) << " bytes" << std::endl;

    return 0;
}