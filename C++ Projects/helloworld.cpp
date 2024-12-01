#include <iostream>

int main() {

    // arrays = a collection of elements of the same type
    //          can store multiple values in a single variable
    //          can be accessed using an index

    std::string car[] = {"Lexus", "Toyota", "Honda", "Ford"};

    std::cout << car[0] << std::endl;
    std::cout << car[1] << std::endl;
    std::cout << car[2] << std::endl;
    std::cout << car[3] << std::endl;

    return 0;
}