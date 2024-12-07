#include <iostream>

// function template = a function that can be called with different parameter types
//                    can be used to create generic functions
//                    useful for creating reusable code
//                    can be used to create overloaded functions    
//                    can be used to create generic classes

// instead of all that repetition, you can use a function template
// template parameter declaration = a parameter that is used to specify the type of data that is passed to the function
template <typename T>
// must be declared before the function template definition
T max(T a, T b) {
    return a > b ? a : b;
}

int main() {

    std::cout << max('1', '2') << std::endl;    

    return 0;
}