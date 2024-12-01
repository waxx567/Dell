#include <iostream>

void printNum();

int main() {

    // local variables = variables that are defined inside a function or block of code
    // global variables = variables that are defined outside of a function or block of code and can be accessed from anywhere in the program

    int myNum = 1;

    printNum();

    return 0;
}
void printNum() {
    int myNum = 2;
    std::cout << myNum << std::endl;
}