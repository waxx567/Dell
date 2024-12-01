#include <iostream>

void bakePizza();
void bakePizza(std::string topping1);
void bakePizza(std::string topping1, std::string topping2);

int main() {

    // overloaded functions = functions with the same name but different parameters
    //                        or different return types

    bakePizza("pepperoni", "mushroom");

    return 0;
}

void bakePizza() {
    std::cout << "Here is your pizza!" << std::endl;
}
void bakePizza(std::string topping1) {
    std::cout << "Here is your " << topping1 << " pizza!" << std::endl;
} 
void bakePizza(std::string topping1, std::string topping2) {
    std::cout << "Here is your " << topping1 << " and " << topping2 << " pizza!" << std::endl;
}