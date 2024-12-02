#include <iostream>

void swap(std::string& x, std::string& y);

int main() {

    // pass by value = pass the value of an object by reference
    // pass by reference = pass the address of an object by reference

    std::string x = "Cool";
    std::string y = "Uncool";
    
    swap(x, y);

    std::cout << x << '\n';
    std::cout << y << '\n';

    return 0;
}

void swap(std::string& x, std::string& y) {
    std::string temp = x;
    x = y;
    y = temp;
}