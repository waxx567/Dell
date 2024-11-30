#include <iostream>
#include <cmath>

int main() {
    
    // switch = another example

    char grade;

    std::cout << "Enter your grade: ";
    std::cin >> grade;

    switch (grade) {
        case 'A':
            std::cout << "You got an A!" << std::endl;
            break;
        case 'B':
            std::cout << "You got a B!" << std::endl;
            break;
        case 'C':
            std::cout << "You got a C!" << std::endl;
            break;
        case 'D':
            std::cout << "You got a D!" << std::endl;
            break;
        case 'F':
            std::cout << "You got an F!" << std::endl;
            break;
        default:
            std::cout << "Invalid grade!" << std::endl;
            break;
    }

    return 0;
}