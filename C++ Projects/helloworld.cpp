#include <iostream>

int main() {
    
    double x = 3;
    double y = 4;
    double z;

    // z = std::max(x, y); // z = 4
    z = std::min(x, y); // z = 3

    std::cout << z;

    return 0;
}