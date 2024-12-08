#include <iostream>

enum name {
    Wayne,
    John,
    Jane,
    Bob
};

// other examples

enum Flavors {
    VANILLA,
    CHOCOLATE,
    STRAWBERRY,
    RASPBERRY
};

enum Colors {
    RED,
    GREEN,
    BLUE
};

enum Days {
    MONDAY = 1,
    TUESDAY = 2,
    WEDNESDAY = 3,
    THURSDAY = 4,
    FRIDAY = 5
};

enum parts {
    gearlever = 56437,
    steeringwheel = 97543,
    seat = 12345,
    engine = 23456,
    transmission = 34567,
    exhaust = 45678,
    brake = 56789,
    clutch = 67890
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

    return 0;
}