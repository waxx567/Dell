#include <iostream>

/**
 * @brief Demonstrates the use of pointers in C++.
 *
 * @details This function initializes a string variable and a pointer 
 *          to that string, then prints the address stored in the pointer.
 *
 * @return 0 on successful execution.
 */
int main() {

    std::string name = "Wayne";
    int age = 30;
    std::string pizzas[5] = {"Pepperoni", "Hawaiian", "Mushroom", "Vegetarian", "Cheese"};

    std::string *namePtr = &name;
    int *agePtr = &age;
    // the array is a pointer to the first element
    // so no need for & (the address of operator)
    std::string *pizzasPtr = pizzas;

    // prints the value at the address
    std::cout << *namePtr << std::endl;
    std::cout << *agePtr << std::endl;

    return 0;
}