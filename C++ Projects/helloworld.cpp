#include <iostream>

/**
 * @brief Main entry point of the program
 *
 * This function creates an array of SIZE elements and fills it with the string "Triumph".
 * It then prints out each element of the array to the console.
 *
 * @return 0 on successful execution
 */
int main() {

    const int SIZE = 100;

    std::string bikes[SIZE];

    fill(bikes, bikes + SIZE, "Triumph");

    for (std::string bike : bikes) {
        std::cout << bike << std::endl;
    }

    return 0;
}