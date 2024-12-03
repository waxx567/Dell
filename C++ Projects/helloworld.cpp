#include <iostream>

int main() {

    // pointer = a variable that holds the address of another variable
    // & = the address of operator
    // * = the dereference operator
    // int* = the type of the pointer
    // int = the type of the variable that the pointer points to

    std::string name = "Wayne";
    std::string *namePtr = &name;

    std::cout << namePtr << std::endl;

    return 0;
}