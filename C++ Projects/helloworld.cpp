#include <iostream>

int main() {

    // break = used to exit a loop
    // continue = used to skip an iteration of a loop

    for (int i = 1; i <= 20; i++) {
        if (i == 13)
        {
            break;
        }
        
        std::cout << i << std::endl;
    }

    return 0;
}