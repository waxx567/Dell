#include <iostream>

int main() {

    // pass by value = pass the value of an object by reference
    // pass by reference = pass the address of an object by reference

    std::string x = "Cool";
    std::string y = "Uncool";
    std::string temp;

    temp = x;
    x = y;
    y = temp;

    std::cout << x << '\n';
    std::cout << y << '\n';

    return 0;
}