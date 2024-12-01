#include <iostream>

double square(double length);

int main() {

    // return type = the type of the value that the function returns
    // return a value back to the place where you called the function
    // void = does not return any value

    double length = 5.0;
    double area = square(length);

    std::cout << "The area of the square is: " << area << "cm^2" << std::endl;
    
    return 0;
}

double square(double length) {
    return length * length;
}