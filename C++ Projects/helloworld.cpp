#include <iostream>

// factorial function = a function that multiplies a number by itself

int factorial(int n);

int main() {
    
    std::cout << factorial(10) << std::endl;

    return 0;
}

int factorial(int n) {
    if(n > 1) {
        return n * factorial(n - 1);
    }
    else {
        return 1;
    }
}