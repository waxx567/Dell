#include <iostream>

int main() {

    // && = checks if both conditions are true
    // || = checks if either condition is true
    // ! = checks if the condition is false

    bool sunny = true;

    if (!sunny) {
        std::cout << "It's cloudy" << std::endl;
    }
    else {
        std::cout << "It's sunny" << std::endl;
    }
    
    return 0;
}