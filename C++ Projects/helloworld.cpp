#include <iostream>
#include <ctime>

int main() {

    // pseudo-random number generator 
    srand(time(NULL)); // seed the random number generator with the current time

    int num = rand() % 6; // generate a random number between 0 and 5 

    std::cout << num << std::endl;

    return 0;
}