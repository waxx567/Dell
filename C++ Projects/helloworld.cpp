#include <iostream>
#include <ctime>

int main() {

    // random event generator
    srand(time(0)); // seed the random number generator with the current time
    int randNum = rand() % 5 + 1; // generate a random number between 1 and 5

    switch (randNum)
    {
    case 1: 
        std::cout << "You got a 1!" << std::endl;
        break;

    case 2: 
        std::cout << "You got a 2!" << std::endl;
        break;

    case 3: 
        std::cout << "You got a 3!" << std::endl;
        break;  

    case 4: 
        std::cout << "You got a 4!" << std::endl;
        break;

    case 5: 
        std::cout << "You got a 5!" << std::endl;
        break;
    
    default:
        break;
    }

    return 0;
}