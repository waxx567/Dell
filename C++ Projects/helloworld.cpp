#include <iostream>

int main() {

    // nested loops = a loop within a loop
    // outer loop = the loop that contains the inner loop
    // inner loop = the loop that is contained within the outer loop

    for (int i = 1; i <= 3; i++) {
        for (int j = 1; j <= 3; j++) {
            std::cout << i << " " << j << std::endl;
        }
    }

    return 0;
}