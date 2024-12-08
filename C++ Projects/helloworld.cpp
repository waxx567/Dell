#include <iostream>

// pass a struct to a function

// to pass the original struct to the function

struct Car {
    std::string make;
    std::string model;
    int year;
    std::string color;
};

void displayCar(Car &car);
void paintCar(Car &car, std::string color);

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

    // display the address of car1
    std::cout << "Car1 address: " << &car1 << std::endl;
    // display the address of car2
    std::cout << "Car2 address: " << &car2 << std::endl;
    displayCar(car1);
    displayCar(car2);

    return 0;
}
void displayCar(Car &car) {
    // display the addresses of the members passed to the function
    std::cout << "Car address: " << &car << std::endl;
    std::cout << "Make: " << car.make << std::endl;
    std::cout << "Model: " << car.model << std::endl;
    std::cout << "Year: " << car.year << std::endl;
    std::cout << "Color: " << car.color << std::endl;
}
void paintCar(Car &car, std::string color) {
    car.color = color;
}