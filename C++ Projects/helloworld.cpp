#include <iostream>

int main() {
    
    // accepting user input
    // if you type a string that has spaces, it will stop reading the string at the first space
    std::string name;
    int age;

    std::cout << "Enter your full name: ";
    std::getline(std::cin, name); 

    std::cout << "How old are you? ";
    std::cin >> age;

    std::cout << "Hello, " << name << "!" << std::endl;
    std::cout << "You are " << age << " years old." << std::endl;

    return 0;
}