#include <iostream> 

int main() {
    
    // The const keyword specifies that a variable's value is constant
    // tells the compiler to prevent anything from modifying it
    // (read-only)

    // Create a program to calculate the circumference of a circle
    const double PI = 3.14159;
    PI = 420.69;
    double radius = 10;
    double circumference = 2 * PI * radius;

    std::cout << circumference << "cm";

    // Adding const will throw an error because the value of PI is constant

    return 0;
}