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

    // to access the temperature variable, we need a getter
    public:
    int getTemperature() {
        return temperature;
    }   
    // if you want to set the temperature, you need a setter (writeable as well as readable)
    void setTemperature(int temp) {
        this->temperature = temp;
    }
};

int main() {

    Stove stove;

    stove.setTemperature(500);

    // but we can access it through the getter
    std::cout << "Temperature: " << stove.getTemperature() << std::endl;

    return 0;
}