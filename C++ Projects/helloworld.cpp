#include <iostream>

int main() {

    // do while loop = executes a block of code repeatedly
    //                  as long as a condition is true

    int number;
    
    do {
        std::cout << "Enter a positive number: ";
        std::cin >> number;
    } while (number < 0);
    
    std::cout << "The number is: " << number << std::endl;

    return 0;
}