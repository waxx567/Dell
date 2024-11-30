#include <iostream>

int main() {

    // && = checks if both conditions are true
    // || = checks if either condition is true
    // ! = checks if the condition is false

    int temp;

    std::cout << "Enter the temperature: ";
    std::cin >> temp;

    if (temp <= 0 || temp >= 30) {
        std::cout << "The temperature is bad" << std::endl;
    }
    else {
        std::cout << "The temperature is bad" << std::endl;
    }
    
    return 0;
}