#include <iostream>

/**
 * @brief Main entry point of the program
 *
 * This function prints out the locations of three car models from the given array, one from each row.
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
        std::cout << models[i] << std::endl;
    }

    return 0;
}