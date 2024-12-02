#include <iostream>

/**
 * @brief The main entry point of the program
 *
 * @details This function initializes an array of strings representing bike brands,
 *          fills the first half of the array with the string "Triumph" and the second
 *          half with the string "Honda". It then iterates over the array and prints
 *          each brand to the console.
 *
 * @return 0 on successful execution
 */
int main() {

    const int SIZE = 100;

    std::string bikes[SIZE];

    fill(bikes, bikes + (SIZE/2), "Triumph");
    fill(bikes + (SIZE/2), bikes + SIZE, "Honda");

    for (std::string bike : bikes) {
        std::cout << bike << std::endl;
    }

    return 0;
}