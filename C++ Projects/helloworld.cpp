#include <iostream>

// recursive function

void walk(int steps);

int main() {
    
    walk(10);

    return 0;
}

void walk(int steps) {
    if(steps > 0) {
        std::cout << "You walk one step" << std::endl;
        walk(steps - 1);
    }
}