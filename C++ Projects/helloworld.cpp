#include <iostream>

// factorial function = a function that multiplies a number by itself

int factorial(int n);

int main() {
    
    std::cout << factorial(10) << std::endl;

    return 0;
}

int factorial(int n) {
    int result = 1;
    for (int i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
}