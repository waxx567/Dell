#include <iostream>

// function template = a function that can be called with different parameter types
//                    can be used to create generic functions
//                    useful for creating reusable code
//                    can be used to create overloaded functions    
//                    can be used to create generic classes

// if you wish to pass in two different data types

// adjust the declaration
template <typename T, typename U>

// adjust the definition
U max(T a, U b) {
    return a > b ? a : b;
}
// changing the return to a double will solve it

int main() {

    std::cout << max(1, 2.1) << std::endl;    

    return 0;
}