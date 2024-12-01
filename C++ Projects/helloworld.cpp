#include <iostream>

void bakePizza();

int main() {

    // overloaded functions = functions with the same name but different parameters
    //                        or different return types

    bakePizza();

    return 0;
}

void bakePizza() {
    std::cout << "Here is your pizza!" << std::endl;
}
void bakePizza(std::string topping1) {
    std::cout << "Here is your " << topping1 << " pizza!" << std::endl;
} 