#include <iostream>

int main() {
    
    // accepting user input
    std::string name;
    int age;

    // to prevent that problem

    std::cout << "How old are you? ";
    std::cin >> age;

    std::cout << "Enter your full name: ";
    // modify this line (ws for whitespace)
    std::getline(std::cin >> std::ws, name);

    std::cout << "Hello, " << name << "!" << std::endl;
    std::cout << "You are " << age << " years old." << std::endl;

    return 0;
}