#include <iostream>

/**
 * @brief Main entry point of the program
 *
 * This function initializes an array of car brands and outputs each brand
 * to the console. The array contains four elements, each representing a
 * different car brand. It then prints each brand on a new line.
 *
 * @return 0 on success
 */
int main() {

    std::string cars[4];

    cars[0] = "Lexus";
    cars[1] = "Mazda";
    cars[2] = "Honda";
    cars[3] = "Ford";

    std::cout << cars[0] << std::endl;
    std::cout << cars[1] << std::endl;
    std::cout << cars[2] << std::endl;
    std::cout << cars[3] << std::endl;

    return 0;
}