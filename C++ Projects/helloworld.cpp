#include <iostream>

/**
 * @brief Main entry point of the program
 *
 * This function initializes an array of prices and outputs each price to the console.
 * The array contains five elements, each representing a different price. The prices
 * are iterated and printed using standard output.
 *
 * @return 0 on successful execution
 */
int main() {
    
    double prices[] = {1.99, 2.99, 3.99, 4.99, 5.99};

    std::cout << prices[0] << std::endl;
    std::cout << prices[1] << std::endl;
    std::cout << prices[2] << std::endl;
    std::cout << prices[3] << std::endl;
    std::cout << prices[4] << std::endl;

    return 0;
}