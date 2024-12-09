#include <iostream>

// overloaded constructors = multiple constructors with the same name but different parameters
// allows fo varying arguments when instantiating an object

class Pizza {
    public:
        std::string topping1;
        std::string topping2;

    Pizza(std::string topping1) {
        this->topping1 = topping1;
    }

    Pizza(std::string topping1, std::string topping2) {
        this->topping1 = topping1;
        this->topping2 = topping2;
    }
};

int main() {

    Pizza pizza1("Pepperoni");
    Pizza pizza2("Mushroom", "Peppers");
    // what if we want a plain pizza with no toppings
    Pizza pizza3;
    // but we still throw an error because Pizza cannot be called with no parameters

    std::cout << pizza2.topping1 << std::endl;
    std::cout << pizza2.topping2 << std::endl;

    return 0;
}