#include <iostream>

int main() {

    // && = checks if both conditions are true
    // || = checks if either condition is true
    // ! = checks if the condition is false

    int temp;

    std::cout << "Enter the temperature: ";
    std::cin >> temp;

    if (temp >= 100 && temp <= 200) {
        std::cout << "It's hot!" << std::endl;
    }
    else if (temp >= 0 && temp <= 100) {
        std::cout << "It's warm!" << std::endl;
    }
    else if (temp >= -100 && temp <= 0) {
        std::cout << "It's cold!" << std::endl;
    }
    
    return 0;
}