#include <iostream>

int main() {

    // ternary operator ?: = replacement to an if/else statement
    // condition ? expression1 : expression2

    int grade = 75;

    // instead of this

    if (grade >= 60)
    {
        std::cout << "You passed!";
    }
    else
    {
        std::cout << "You failed!";
    }
    
    return 0;
}