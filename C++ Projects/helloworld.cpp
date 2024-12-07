#include <iostream>

// recursive function

// this is a very simple example and the trade-off is that it's not very efficient
// it uses a lot of stack space and in this instance, one would probably use the
// for loop instead
// identifying best use case on a case by case basis is essential

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