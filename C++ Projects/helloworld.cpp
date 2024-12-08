#include <iostream>

// pass a struct to a function

// remember thst structs are passed by value not by reference
// therefore a copy of the struct is made and passed

struct Car {
    std::string make;
    std::string model;
    int year;
    std::string color;
};

void displayCar(Car car);

int main() {

    Car car1;
    Car car2;

    car1.make = "Lexus";
    car1.model = "IS300";
    car1.year = 2022;
    car1.color = "Black";

    car2.make = "Honda";
    car2.model = "Civic";
    car2.year = 2021;
    car2.color = "Red";

    displayCar(car1);
    displayCar(car2);

    return 0;
}
void displayCar(Car car) {
    std::cout << "Make: " << car.make << std::endl;
    std::cout << "Model: " << car.model << std::endl;
    std::cout << "Year: " << car.year << std::endl;
    std::cout << "Color: " << car.color << std::endl;
}