#include <iostream>

int main() {

    // arrays = a collection of elements of the same type
    //          can store multiple values in a single variable
    //          can be accessed using an index

    std::string cars[4];

    cars[0] = "Lexus";
    cars[1] = "Mazda";
    cars[2] = "Honda";
    cars[3] = "Ford";

    std::cout << cars[0] << std::endl;
    std::cout << cars[1] << std::endl;
    std::cout << cars[2] << std::endl;
    std::cout << cars[3] << std::endl;

    return 0;
}