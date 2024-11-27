#include <iostream> 

int main() {
    
    // The const keyword specifies that a variable's value is constant
    // tells the compiler to prevent anything from modifying it
    // (read-only)

    // Create a program to calculate the circumference of a circle
    double pi = 3.14159;
    double radius = 10;
    double circumference = 2 * pi * radius;

    // All good but if someone changes the value of pi it will change the result of the program
    pi = 420.69;

    std::cout << circumference << "cm";

    return 0;
}