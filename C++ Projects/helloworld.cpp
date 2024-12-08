#include <iostream>

// function template = a function that can be called with different parameter types
//                    can be used to create generic functions
//                    useful for creating reusable code
//                    can be used to create overloaded functions    
//                    can be used to create generic classes

// if you need to mix and match data types (ie. int and double)
// this will now throw a compiler error

template <typename T>

T max(T a, T b) {
    return a > b ? a : b;
}

int main() {

    std::cout << max(1, 2.1) << std::endl;    

    return 0;
}