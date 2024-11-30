#include <iostream>

int main() {

    // nested loops = a loop within a loop
    // outer loop = the loop that contains the inner loop
    // inner loop = the loop that is contained within the outer loop

    for (int i = 1; i <= 3; i++) {
        for (int j = 1; j <= 10; j++) {
            std::cout << j << ' ';
        }
        std::cout << std::endl;
    }

    return 0;
}