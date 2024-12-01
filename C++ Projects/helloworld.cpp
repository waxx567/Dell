#include <iostream>
#include <ctime>

int main() {

    // pseudo-random number generator (3 dice roll)
    srand(time(NULL)); // seed the random number generator with the current time

    int num1 = rand() % 6 + 1; // generate a random number between 1 and 6
    int num2 = rand() % 6 + 1; // generate a random number between 1 and 6
    int num3 = rand() % 6 + 1; // generate a random number between 1 and 6

    std::cout << num1 << std::endl;
    std::cout << num2 << std::endl;
    std::cout << num3 << std::endl;

    return 0;
}