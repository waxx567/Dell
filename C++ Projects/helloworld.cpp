#include <iostream>

int main() {

    // ternary operator ?: = replacement to an if/else statement
    // condition ? expression1 : expression2

    // int grade = 75;
    // grade >= 60 ? std::cout << "You passed!" : std::cout << "You failed!";

    int number = 6;
    number % 2 ? std::cout << "Number is odd" : std::cout << "Number is even";
    
    return 0;
}