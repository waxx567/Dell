#include <iostream>
#include <cmath>

int main() {

    // using switch
    
    char op;
    double num1;
    double num2;
    double result;

    std::cout << "********** CALCULATOR **********\n";

    std::cout << "Enter one of these (+ - * /): ";
    std::cin >> op;

    std::cout << "Enter #1: ";
    std::cin>> num1;
    
    std::cout << "Enter #2: ";
    std::cin>> num2;

    switch (op)
    {
        case '+':
            result = num1 + num2;
            std::cout << "Result: " << result << std::endl;
            break;
        case '-':
            result = num1 - num2;
            std::cout << "Result: " << result << std::endl;
            break;
        case '*':
            result = num1 * num2;
            std::cout << "Result: " << result << std::endl;
            break;
        case '/':
            result = num1 / num2;
            std::cout << "Result: " << result << std::endl;
            break;
        default:
            std::cout << "Invalid operator" << std::endl;
            break;
    }

    std::cout << "********************************\n";

    return 0;
}