#include <iostream>

/**
 * @brief The main entry point of the program
 *
 * @details This function demonstrates pointers and addresses in C++.
 *          It shows how to declare and use pointers and how to use the address of operator (&)
 *          and the dereference operator (*).
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
    std::cout << *pizzasPtr << std::endl;

    return 0;
}