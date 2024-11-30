#include <iostream>

int main() {

    // useful string methods
    std::string name;
    
    std::cout << "Enter your name: ";
    std::getline(std::cin, name);

    //name.append(" "); // adds a space to the end of the string

    name.append("@gmail.com");

    std::cout << "Your email is: " << name << std::endl;

    return 0;
}