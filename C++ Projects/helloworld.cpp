#include <iostream>

// overloaded constructors = multiple constructors with the same name but different parameters
// allows fo varying arguments when instantiating an object

class Pizza {
    public:
        std::string topping1;

    Pizza(std::string topping1) {
        this->topping1 = topping1;
    }
};

int main() {

    Pizza pizza1("Pepperoni");

    std::cout << pizza1.topping1 << std::endl;

    return 0;
}