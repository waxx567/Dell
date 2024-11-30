#include <iostream>

int main() {

    // useful string methods
    std::string name;
    
    std::cout << "Enter your name: ";
    std::getline(std::cin, name);

    // name.at() returns the character at the specified index

    std::cout << "Your initial is: " << name.at(0) << std::endl;
    
    return 0;
}