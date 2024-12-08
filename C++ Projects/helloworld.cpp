#include <iostream>

// objects 
// assigning default values

class Person {
    public:
        std::string name = "Fred";
        int age = 71;
        bool isMale = true;

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
    Person person2;

    std::cout << person1.name << std::endl;
    std::cout << person1.age << std::endl;
    std::cout << person1.isMale << std::endl;

    std::cout << person2.name << std::endl;
    std::cout << person2.age << std::endl;
    std::cout << person2.isMale << std::endl;

    return 0;
}