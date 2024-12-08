#include <iostream>

// so use an enum
enum name {
    Wayne = 0,
    John = 1,
    Jane = 2,
    Bob = 3
};

int main() {

    name firstName = Wayne;

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

    return 0;
}