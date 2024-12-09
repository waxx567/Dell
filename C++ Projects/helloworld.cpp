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
    public:
    void bark() {
        std::cout << "The dog is barking." << std::endl;
    }
};
class Cat : public Animal {
    public:
    void meow() {
        std::cout << "The cat goes meow." << std::endl;
    }
};

int main() {

    Dog dog;
    Cat cat;

    std::cout << dog.isAlive << std::endl;
    dog.eat();
    dog.bark();

    std::cout << cat.isAlive << std::endl;
    cat.eat();
    cat.meow();

    // of course, cats can't bark and dogs can't meow

    return 0;
}