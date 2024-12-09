#include <iostream>

// abstraction = hiding the implementation details of a class or function
//               from the user
// getter = a function that returns the value of a private member variable
// setter = a function that sets the value of a private member variable

class Stove {
    public:
        int temperature = 0;
    
};

int main() {

    Stove stove;
    // since temperature is public, it is accessible outside the class and can be modified
    stove.temperature = 500;

    std::cout << "Temperature: " << stove.temperature << std::endl;

    return 0;
}