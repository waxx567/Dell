#include <iostream>

/**
 * @brief Main entry point of the program
 *
 * This function initializes a 2D array of strings representing car models and
 * outputs each model to the console. The size of the array is determined at
 * compile time using the sizeof operator.
 *
 * @return 0 on successful execution
 */
int main() {

    std::string models[][3] = {
        {"Focus", "Fusion", "Ranger"},
        {"Civic", "Accord", "CRV"},
        {"Camry", "Corolla", "RAV4"}
    };

    int rows = sizeof(models) / sizeof(models[0]);
    int columns = sizeof(models[0]) / sizeof(models[0][0]);

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < columns; j++) {
            std::cout << models[i][j] << " ";
        }
    }

    return 0;
}