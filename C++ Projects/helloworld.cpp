#include <iostream>

int main() {

    // memory address = the location in memory where a variable is stored
    //                  address can be accessed using the & symbol

    std::string name = "Wayne";
    int age = 30;
    bool isMale = true;

    std::cout << "Name: " << &name << std::endl;

    return 0;
}