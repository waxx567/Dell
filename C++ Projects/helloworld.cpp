#include <iostream>

/**
 * @brief The main entry point of the program
 *
 * @details This function initializes an array of strings representing bike brands,
 *          fills the first third of the array with the string "Triumph", the second
 *          third with the string "Honda", and the final third with the string "Ducati". It
 *          then iterates over the array and prints each brand to the console.
 *
 * @return 0 on successful execution
 */
int main() {

    const int SIZE = 99;

    std::string bikes[SIZE];

    fill(bikes, bikes + (SIZE/3), "Triumph");
    fill(bikes + (SIZE/3), bikes + (SIZE/3)*2, "Honda");
    fill(bikes + (SIZE/3)*2, bikes + SIZE, "Ducati");

    for (std::string bike : bikes) {
        std::cout << bike << std::endl;
    }

    return 0;
}