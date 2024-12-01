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
    
    double prices[5];

    prices[0] = 10.99;
    prices[1] = 12.50;
    prices[2] = 9.99;
    prices[3] = 7.50;
    prices[4] = 6.00;

    std::cout << prices[0] << std::endl;
    std::cout << prices[1] << std::endl;
    std::cout << prices[2] << std::endl;
    std::cout << prices[3] << std::endl;
    std::cout << prices[4] << std::endl;

    return 0;
}