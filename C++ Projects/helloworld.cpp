#include <iostream>

int main() {

    // useful string methods
    std::string name;
    
    std::cout << "Enter your name: ";
    std::getline(std::cin, name);

    // name.length(); // returns the number of characters in the string
    // name.empty(); // returns true if the string is empty, false if not
    // name.find(" "); // returns the index of the first space in the string

    if (name.find(" ") != std::string::npos)
    {
        std::cout << "Invalid name" << std::endl;
    }
    else
    {
        std::cout << "Welcome, " << name << "." << std::endl;
    }
    
    return 0;
}