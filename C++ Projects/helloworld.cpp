#include <iostream>
#include <cmath>

int main() {
    
    // if statements = do something if a condition is true
    //                 do something else if another condition is true
    //                 or do something else if both are false

    int age;

    std::cout << "Enter your age: ";
    std::cin >> age;

    if (age >= 18) {
        std::cout << "You are an adult." << std::endl;
    }
    else if (age >= 13) {
        std::cout << "You are a teenager." << std::endl;
    }
    else {
        std::cout << "You are a child." << std::endl;
    }   

    return 0;
}