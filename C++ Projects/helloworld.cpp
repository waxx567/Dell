#include <iostream>

double square(double length);
double cube(double length);

int main() {

    // return type = the type of the value that the function returns
    // return a value back to the place where you called the function
    // void = does not return any value

    double length = 5.0;
    double area = square(length);
    double volume = cube(length);

    std::cout << "The area of the square is: " << area << "cm^2" << std::endl;
    std::cout << "The volume of the cube is: " << volume << "cm^3" << std::endl;
    
    return 0;
}

double square(double length) {
    return length * length;
}

double cube(double length) {
    return length * length * length;
}