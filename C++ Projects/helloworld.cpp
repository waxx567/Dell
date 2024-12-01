#include <iostream>

/**
 * @brief Main entry point of the program
 *
 * This function initializes an array of grade characters and outputs each
 * grade to the console using a for loop.
 *
 * @return 0 on successful execution
 */
int main() {

    char grades[] = {'A', 'B', 'C', 'D', 'F'};

    for (int i = 0; i < sizeof(grades)/sizeof(char); i++) {
        std::cout << grades[i] << std::endl;
    }

    return 0;
}