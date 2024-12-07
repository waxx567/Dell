#include <iostream>

// function template = a function that can be called with different parameter types
//                    can be used to create generic functions
//                    useful for creating reusable code
//                    can be used to create overloaded functions    
//                    can be used to create generic classes

int max(int a, int b) {
    return a > b ? a : b;
}

int main() {

    // if you want to use doubles, the result is truncated
    std::cout << max(1.1, 2.2) << std::endl;    

    return 0;
}