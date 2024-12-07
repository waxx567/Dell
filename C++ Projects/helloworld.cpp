#include <iostream>

// iterative function

void walk(int steps);

int main() {
    
    walk(10);

    return 0;
}

void walk(int steps) {
    for (int i = 0; i < steps; i++) {
        std::cout << "You walk one step" << std::endl;
    }
}