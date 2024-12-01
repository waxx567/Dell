#include <iostream>

/**
 * @brief Main entry point of the program
 *
 * This function initializes an array of grade characters and outputs the
 * number of elements in the array. The size of the array is determined by
 * dividing the total byte size of the array by the byte size of a single 
 * char element.
 *
 * @return 0 on successful execution
 */
int main() {

    char grades[] = {'A', 'B', 'C', 'D', 'F'};

    std::cout << sizeof(grades)/sizeof(char) << " elements" << std::endl;

    return 0;
}