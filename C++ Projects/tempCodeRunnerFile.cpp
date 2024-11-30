#include <iostream>

int main() {

    // create a temperature converter

    double temp;
    char unit;

    std::cout << "Enter the temperature: ";
    std::cin >> temp;

    std::cout << "Enter the unit: ";
    std::cin >> unit;

    if (unit == 'C' || unit == 'c') {
        temp = temp * 1.8 + 32;
        std::cout << temp << "F";
    }
    else if (unit == 'F' || unit == 'f') {    
        temp = (temp - 32) / 1.8;
        std::cout << temp << "C";
    }
    else {
        std::cout << "Invalid unit";
    }
    
    return 0;
}