#include <iostream>

void happyBirthday(std::string name, int age);
int main() {

    // function = a block of reuseable code that performs a specific task

    std::string name;
    int age = 21;
    
    std::cout << "Enter your name: ";
    std::getline(std::cin, name);

    happyBirthday(name, age);
    
    return 0;
}

void happyBirthday(std::string name, int age) {
    std::cout << "Happy birthday to you!" << std::endl;
    std::cout << "Happy birthday to you!" << std::endl;
    std::cout << "Happy birthday, dear " << name << "!" << std::endl;
    std::cout << "Happy birthday to you!" << std::endl;
    std::cout << "You are " << age << " years old today." << std::endl;
}