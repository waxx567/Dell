#include <iostream>

std::string concatStrings(std::string a, std::string b);

int main() {

    std::string firstName = "Wayne";
    std::string lastName = "McRae";

    std::cout << "Full name: " << concatStrings(firstName, lastName) << std::endl;

    return 0;
}

std::string concatStrings(std::string a, std::string b) {

    return a + " " + b;
}