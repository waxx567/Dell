#include <iostream>

void happyBirthday(std::string name);
int main() {

    // function = a block of reuseable code that performs a specific task

    std::string name;
    
    std::cout << "Enter your name: ";
    std::getline(std::cin, name);

    happyBirthday(name);
    
    return 0;
}

void happyBirthday(std::string name) {
    std::cout << "Happy birthday to you!" << std::endl;
    std::cout << "Happy birthday to you!" << std::endl;
    std::cout << "Happy birthday, dear " << name << "!" << std::endl;
    std::cout << "Happy birthday to you!" << std::endl;
}