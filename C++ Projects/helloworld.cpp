#include <iostream>
#include <ctime>

int main() {

    // pseudo-random number generator 
    srand(time(NULL)); // seed the random number generator with the current time

    int num = rand() % 6 + 1; // generate a random number between 1 and 6

    std::cout << num << std::endl;

    return 0;
}