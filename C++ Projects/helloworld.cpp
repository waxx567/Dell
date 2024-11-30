#include <iostream>

int main() {

    // useful string methods
    std::string name;
    
    std::cout << "Enter your name: ";
    std::getline(std::cin, name);

    // name.length(); // returns the number of characters in the string
    // name.empty(); // returns true if the string is empty, false if not
    // name.find(" "); // returns the index of the first space in the string

    if (name.length() > 16)
    {
        std::cout << "Your name is too long" << std::endl;
    }
    else
    {
        std::cout << "Welcome, " << name << "." << std::endl;
    }
    
    
    return 0;
}