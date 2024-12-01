#include <iostream>

/**
 * @brief Main entry point of the program
 *
 * The function calculates and prints the size of a double
 * variable in bytes using the sizeof() operator.
 */
int main() {

    double pi = 3.14159;

    std::cout << sizeof(pi) << " bytes" << std::endl;

    return 0;
}