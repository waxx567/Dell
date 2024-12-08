#include <iostream>

// so use an enum
enum name {
    Wayne = 0,
    John = 1,
    Jane = 2,
    Bob = 3
};

int main() {

    name firstName = Jane;

    switch (firstName) {
    case 0:
        std::cout << "Wayne" << std::endl;
        break;
    case 1:
        std::cout << "John" << std::endl;
        break;
    case 2:
        std::cout << "Jane" << std::endl;
        break;
    case 3:
        std::cout << "Bob" << std::endl;
        break;
    default:
        std::cout << "Unknown" << std::endl;
        break;
    }

    return 0;
}