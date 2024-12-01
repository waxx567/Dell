#include <iostream>

/**
 * @brief Main entry point of the program
 *
 * This function initializes an array of grades and outputs each grade to the console.
 * It uses a range-based for loop to iterate through the array and print each grade.
 *
 * @return 0 on successful execution
 */
int main() {

    int grades[] = {100, 90, 80, 70, 60};

    for (int grade : grades) {
        std::cout << grade << std::endl;
    }

    return 0;
}