#include <iostream>

int myNum = 3;

void printNum();

int main() {

    printNum();
    int myNum = 1;
    // use :: to access global variable
    std::cout << ::myNum << std::endl;

    return 0;
}
void printNum() {
    int myNum = 2;
    std::cout << myNum << std::endl;
}