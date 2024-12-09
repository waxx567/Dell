#include <iostream>

// abstraction = hiding the implementation details of a class or function
//               from the user
// getter = a function that returns the value of a private member variable
// setter = a function that sets the value of a private member variable

class Stove {
    // setting the class attributes to private
    // so they can only be accessed from within the class
    private:
        int temperature = 0;
    
};

int main() {

    Stove stove;

    stove.temperature = 500;

    std::cout << "Temperature: " << stove.temperature << std::endl;
    // now the programmer can't access the temperature variable

    return 0;
}