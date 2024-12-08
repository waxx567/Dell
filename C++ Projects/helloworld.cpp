#include <iostream>

// constructor = functions that are used to create an object
//               they are used to initialize the object
//               they are used to set the initial values of the object
//               they are used to perform actions on the object
//               special methods that are called when an object is instantiated
//               useful for assigning values to attributes as arguments

class Motorcycle {
    public:
        std::string make;
        std::string model;
        int year;
        std::string color;
        std::string licensePlate;

        // constructors can also be set up like this
        Motorcycle(std::string v, std::string w, int x, std::string y, std::string z) {
            make = v;
            model = w;
            year = x;
            color = y;
            licensePlate = z;
        }
};

int main() {

    Motorcycle motorcycle1("Triumph", "Street Triple", 2023, "Yellow", "W4YN3M");

    std::cout << "Make: " << motorcycle1.make << std::endl;
    std::cout << "Model: " << motorcycle1.model << std::endl;
    std::cout << "Year: " << motorcycle1.year << std::endl;
    std::cout << "Color: " << motorcycle1.color << std::endl;
    std::cout << "License Plate: " << motorcycle1.licensePlate << std::endl;

    return 0;
}