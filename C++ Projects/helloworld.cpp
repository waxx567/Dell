#include <iostream>

int main() {

    // useful string methods
    std::string name;
    
    std::cout << "Enter your name: ";
    std::getline(std::cin, name);

    // name.length(); // returns the number of characters in the string
    // name.empty(); // returns true if the string is empty, false if not
    // name.find(" "); // returns the index of the first space in the string
    // name.clear(); // clears the string

    std::string name;
    
    std::cout << "Enter your name: ";
    std::getline(std::cin, name);

    name.clear();

    std::cout << "Hello " << name << "!" << std::endl;

    return 0;
}