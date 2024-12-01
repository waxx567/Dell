#include <iostream>

/**
 * @brief Main entry point of the program
 *
 * This function demonstrates how to use a foreach loop to iterate over an array of
 * strings and print each string to the console.
 *
 * @return 0 on successful execution
 */
int main() {

    // foreach loop = executes a block of code for each element in a container
    //                can use a variable to iterate through the container

    std::string cars[] = {"Lexus", "Toyota", "Honda", "Ford"};

    for (std::string car : cars) {
        std::cout << car << std::endl;
    }

    return 0;
}