#include <iostream>

/**
 * @brief Main entry point of the program
 *
 * This function prints out three car models from the given array, one from each row.
 */
int main() {

    std::string models[][3] = {
        {"Focus", "Fusion", "Ranger"},
        {"Civic", "Accord", "CRV"},
        {"Camry", "Corolla", "RAV4"}
    };

    std::cout << models[0][0] << std::endl;
    std::cout << models[1][1] << std::endl;
    std::cout << models[2][2] << std::endl; 

    return 0;
}