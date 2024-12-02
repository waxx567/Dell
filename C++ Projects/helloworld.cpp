#include <iostream>

/**
 * @brief Main entry point of the program
 *
 * This function initializes a 2D array with car models and prints
 * each model in a formatted manner. It calculates the number of rows
 * and columns in the array, then iterates over each element, displaying
 * them in a tabular format.
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
        std::cout << std::endl;
    }

    return 0;
}