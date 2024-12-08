#include <iostream>

// this is more readable

enum name {
    Wayne,
    John,
    Jane,
    Bob
};

int main() {

    name firstName = Jane;

    switch (firstName) {
    case Wayne:
        std::cout << "Wayne" << std::endl;
        break;
    case John:
        std::cout << "John" << std::endl;
        break;
    case Jane:
        std::cout << "Jane" << std::endl;
        break;
    case Bob:
        std::cout << "Bob" << std::endl;
        break;
    default:
        std::cout << "Unknown" << std::endl;
        break;
    }

    // if you don't assign values to the enum, tey will be automatically assigned

    return 0;
}