#include <iostream>

/**
 * @brief Main entry point of the program
 *
 * This function initializes an array of car brands and outputs the number
 * of elements in the array. The size of the array is determined by dividing
 * the total byte size of the array by the byte size of a single std::string
 * element.
 *
 * @return 0 on successful execution
 */
int main() {

    std::string cars[] = {"Lexus", "Mazda", "Honda", "Ford"};

    std::cout << sizeof(cars)/sizeof(std::string) << " elements" << std::endl;

    return 0;
}