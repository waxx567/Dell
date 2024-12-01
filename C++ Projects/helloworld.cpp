#include <iostream>

int myNum = 3;

void printNum();

int main() {

    printNum();

    return 0;
}
void printNum() {
    std::cout << myNum << std::endl;
}