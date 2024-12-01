#include <iostream>

int main() {

    // iterate over elements in an array
    std::string cars[4] = {"Lexus", "Mazda", "Honda", "Ford"};

    for (int i = 0; i < 4; i++) {
        std::cout << cars[i] << std::endl;
    }

    return 0;
}