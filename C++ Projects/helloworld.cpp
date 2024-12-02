#include <iostream>

int main() {
    
    // fill() = used to fill a container with a specific value
    //          fill(begin, end, value)

    std::string bikes[10] = {"Suzuki", "Honda", "Yamaha", "Kawasaki", "BMW", "Triumph", "Aprilia", "KTM", "MV Agusta", "Ducati"};

    for (std::string bike : bikes) {
        std::cout << bike << std::endl;
    }

    return 0;
}