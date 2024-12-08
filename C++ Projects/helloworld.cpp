#include <iostream>

class Car {
    public:
        std::string make;
        std::string model;
        int year;
        std::string color;

        void accelerate() {
            std::cout << "The " << make << " is accelerating" << std::endl;
        }
        void brake() {
            std::cout << "The " << make << " is braking" << std::endl;
        }
};

int main() {

    Car car1;
    car1.make = "Lexus";
    car1.model = "IS300";
    car1.year = 2022;
    car1.color = "White";

    std::cout << "Make: " << car1.make << std::endl;
    std::cout << "Model: " << car1.model << std::endl;
    std::cout << "Year: " << car1.year << std::endl;
    std::cout << "Color: " << car1.color << std::endl;

    car1.accelerate();
    car1.brake();

    return 0;
}