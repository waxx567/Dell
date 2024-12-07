#include <iostream>

// function template = a function that can be called with different parameter types
//                    can be used to create generic functions
//                    useful for creating reusable code
//                    can be used to create overloaded functions    
//                    can be used to create generic classes

int max(int a, int b) {
    return a > b ? a : b;
}

double max(double a, double b) {
    return a > b ? a : b;
}

int main() {

    // what about characters?
    std::cout << max('1', '2') << std::endl;    
    // this w

    return 0;
}