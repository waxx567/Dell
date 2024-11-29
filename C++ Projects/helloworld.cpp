#include <iostream>
#include <cmath>

int main() {
    
    // calculate the hypotenuse of a right triangle
    double a;
    double b;
    double c;
    // solution: c is the square root of a squared + b squared

    std::cout << "Enter the length of side a: ";
    std::cin >> a;

    std::cout << "Enter the length of side b: ";
    std::cin >> b;

    a = pow(a, 2);
    b = pow(b, 2);
    c = sqrt(a + b);

    std::cout << "The length of the hypotenuse is: " << c << std::endl;


    return 0;
}