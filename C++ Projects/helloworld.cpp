#include <iostream>

int main() {

    // do while loop = executes a block of code repeatedly
    //                  as long as a condition is true

    int number;
    
    std::cout << "Enter a positive number: ";
    std::cin >> number;

    while (number < 0)
    {
        std::cout << "Enter a positive number: ";
        std::cin >> number;
    }
    
    std::cout << "The number is: " << number << std::endl;

    // this works but it is repetitive

    return 0;
}