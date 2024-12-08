#include <iostream>

// objects = instances of classes
//          can be used to store data
//          can be used to perform actions
//          can be used to represent real-world entities
// to create an object, you must create a class
// classes act as blueprints for creating objects

class Person {
    public:
        std::string name;
        int age;
        bool isMale;

        // methods = functions that belong to a class
        //          can be used to perform actions on the object
        void eat() {
            std::cout << name << " is eating" << std::endl;
        }
        void drink() {
            std::cout << name << " is drinking" << std::endl;
        }
        void sleep() {
            std::cout << name << " is sleeping" << std::endl;
        }
};

int main() {

    Person person1;

    person1.name = "Karl";
    person1.age = 30;
    person1.isMale = true;
    
    std::cout << person1.name << std::endl;
    std::cout << person1.age << std::endl;
    std::cout << person1.isMale << std::endl;

    person1.eat();

    return 0;
}