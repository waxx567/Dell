#include <iostream>
#include <ctime>

int main() {

    // pseudo-random number generator 
    srand(time(NULL)); // seed the random number generator with the current time

    int num = rand(); // generate a random number between 0 and 32767

    std::cout << num << std::endl;

    return 0;
}