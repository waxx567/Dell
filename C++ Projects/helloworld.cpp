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
// so another overloaded function with the new data type
char max(char a, char b) {
    return a > b ? a : b;
}

int main() {

    std::cout << max('1', '2') << std::endl;    

    return 0;
}