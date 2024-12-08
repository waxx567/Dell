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
    Car car2;

    car1.make = "Lexus";
    car1.model = "IS300";
    car1.year = 2022;
    car1.color = "White";

    car2.make = "Honda";
    car2.model = "Civic";
    car2.year = 2021;
    car2.color = "Red";

    std::cout << "Make: " << car1.make << std::endl;
    std::cout << "Model: " << car1.model << std::endl;
    std::cout << "Year: " << car1.year << std::endl;
    std::cout << "Color: " << car1.color << std::endl;

    std::cout << "Make: " << car2.make << std::endl;
    std::cout << "Model: " << car2.model << std::endl;
    std::cout << "Year: " << car2.year << std::endl;
    std::cout << "Color: " << car2.color << std::endl;

    car1.accelerate();
    car1.brake();

    car2.accelerate();
    car2.brake();

    return 0;
}