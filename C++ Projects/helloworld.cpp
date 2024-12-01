#include <iostream>

/**
 * @brief Main entry point of the program
 *
 * The function calculates and prints the size of a double
 * variable in bytes using the sizeof() operator.
 */
int main() {

    double pi = 3.14159;
    int size = sizeof(pi);

    std::cout << "The size of pi is: " << size << " bytes" << std::endl;

    return 0;
}