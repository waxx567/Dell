#include <iostream>

int main() {

    // while loops = execute a block of code as long as a condition is true

    std::string name;

    while (name.empty())
    {
        std::cout << "Enter your name: ";
        std::getline(std::cin, name);
    }

    std::cout << "Hello, " << name << "!" << std::endl;
    

    return 0;
}