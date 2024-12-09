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
        // within the steer, we can add additional logic or validation
        if (temp < 0) {
            this->temperature = 0;
        }
        else if(temp > 280) {
            std::cout << "The temperature is too high" << std::endl;   
            break;         
        }
        else {
            this->temperature = temp;
        }
    }
};

/**
 * @brief The main entry point of the program.
 *
 * @details This function demonstrates the use of a class with private
 *          member variables and public getter and setter methods. It
 *          creates an instance of the Stove class, sets its temperature
 *          using the setter method, and prints the temperature using the
 *          getter method.
 *
 * @return 0 on successful execution.
 */
int main() {

    Stove stove;

    stove.setTemperature(500);

    // but we can access it through the getter
    std::cout << "Temperature: " << stove.getTemperature() << std::endl;

    return 0;
}