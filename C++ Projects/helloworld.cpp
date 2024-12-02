#include <iostream>

// prevent unwanted changes by adding const to the parameters

void printInfo(const std::string name, const int age);

int main() {

    // const parameters = parameters that cannot be changed after the function has been called
    //                    they are used to prevent the function from modifying the original value of the parameter
    //                    code is more secure and conveys intent better
    //                    useful for reference and pointers

    std::string name = "Wayne";
    int age = 57;

    printInfo(name, age);

    return 0;
}

void printInfo(const std::string name, const int age) {
    std::cout << "Name: " << name << std::endl;
    std::cout << "Age: " << age << std::endl;
}