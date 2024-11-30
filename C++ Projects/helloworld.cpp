#include <iostream>

int main() {

    // useful string methods
    std::string name;
    
    std::cout << "Enter your name: ";
    std::getline(std::cin, name);

    // name.insert(0, "Hello, "); // insert a string at a specific index
    // name.erase(0, 5); // erase a string at a specific index
    std::cout << name << std::endl;

    return 0;
}