#include <iostream>

/**
 * @brief Main entry point of the program
 *
 * This function creates a 2D array of strings and displays the contents of
 * the array to the user.
 *
 * @return 0 if the program is successful, non-zero otherwise.
 */
int main() {

    std::string models[][3] = {
        {"Focus", "Fusion", "Ranger"},
        {"Civic", "Accord", "CRV"},
        {"Camry", "Corolla", "RAV4"}
    };

    std::cout << models[0][0] << " ";
    std::cout << models[0][1] << " ";
    std::cout << models[0][2] << std::endl;

    std::cout << models[1][0] << " ";
    std::cout << models[1][1] << " ";
    std::cout << models[1][2] << std::endl;

    std::cout << models[2][0] << " ";
    std::cout << models[2][1] << " ";
    std::cout << models[2][2] << std::endl; 

    return 0;
}