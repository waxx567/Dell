#include <iostream>
#include <cmath>

int main() {
    
    // if statements = do something if a condition is true
    //                 or do something else if false

    int age;

    std::cout << "Enter your age: ";
    std::cin >> age;

    if (age >= 18) {
        std::cout << "You are an adult." << std::endl;
    }
    else {
        std::cout << "You are a child." << std::endl;
    }   

    return 0;
}