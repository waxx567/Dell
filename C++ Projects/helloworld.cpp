#include <iostream>

// inheritance = when a class receives features from another class
// child class = class that inherits from another class
// parent class = class that is inherited from
// useful to reuse code and reduce code duplication

class Animal {
    public:
    bool isAlive = true;
    void eat() {
        std::cout << "The animal is eating." << std::endl;
    }
};

class Dog : public Animal {
};

int main() {

    Dog dog;

    std::cout << dog.isAlive << std::endl;
    dog.eat();

    return 0;
}