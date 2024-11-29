#include <iostream>

int main() {
    
    // accepting user input
    // cout << (insertion operator)
    // cin >> (extraction operator)
    std::string name;
    int age;

    std::cout << "Enter your name: ";
    std::cin >> name;

    std::cout << "How old are you? ";
    std::cin >> age;

    std::cout << "Hello, " << name << "!" << std::endl;
    std::cout << "You are " << age << " years old." << std::endl;

    return 0;
}