#include <iostream>

/**
 * @brief Main entry point of the program
 *
 * This function initializes an array of car brands and outputs each brand
 * to the console. The array contains four elements, each representing a
 * different brand. The brands are iterated and printed using standard output.
 *
 * @return 0 on successful execution
 */
int main() {

    std::string cars[] = {"Lexus", "Mazda", "Honda", "Ford"};

    for (int i = 0; i < sizeof(cars)/sizeof(std::string); i++) {
        std::cout << cars[i] << std::endl;
    }

    return 0;
}