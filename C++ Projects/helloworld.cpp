#include <iostream>

// this is pass by reference
// we pass the locations and then
// swap the values at the locations

void swap(std::string &x, std::string &y);

/**
 * @brief The main entry point of the program
 *
 * @details This function demonstrates how to swap two strings using pass by
 *          reference. It creates two strings, swaps them using the swap
 *          function, and then prints the swapped strings to the console.
 *
 * @return 0 on success
 */
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

void swap(std::string &x, std::string &y) {
    std::string temp = x;
    x = y;
    y = temp;
}