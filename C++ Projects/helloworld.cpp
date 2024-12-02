#include <iostream>

/**
 * @brief The main entry point of the program
 *
 * @details This function initializes an array of strings, fills the array with
 *          the string "Triumph", and then iterates over the array and prints
 *          each string to the console.
 *
 * @return 0 on successful execution
 */
int main() {

    std::string bikes[100];

    fill(bikes, bikes + 100, "Triumph");

    for (std::string bike : bikes) {
        std::cout << bike << std::endl;
    }

    return 0;
}