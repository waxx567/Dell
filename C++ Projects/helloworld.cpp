#include <iostream>

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