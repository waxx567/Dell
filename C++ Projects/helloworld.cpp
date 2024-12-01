#include <iostream>

/**
 * @brief Main entry point of the program
 *
 * This function initializes an array of grade characters and outputs the size
 * of the array in bytes using the sizeof operator.
 *
 * @return 0 on successful execution
 */
int main() {

    char grades[] = {'A', 'B', 'C', 'D', 'F'};

    std::cout << sizeof(grades) << " bytes" << std::endl;

    return 0;
}