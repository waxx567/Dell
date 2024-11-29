#include <iostream>
#include <cmath>

int main() {
    
    // if statements = do something if a condition is true
    //                 or do nothing if false

    int age;

    std::cout << "Enter your age: ";
    std::cin >> age;

    if (age >= 18) {
        std::cout << "You are an adult." << std::endl;
    }

    return 0;
}