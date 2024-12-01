#include <iostream>
#include <ctime>

int main() {

    // simple number guessing game
    int num;
    int guess;
    int tries;

    srand(time(NULL)); // seed the random number generator with the current time

    num = rand() % 100 + 1; // generate a random number between 1 and 100

    do
    {
        std::cout << "Guess a number between 1 and 100: ";
        std::cin >> guess;
        tries++;

        if (guess > num)
        {
            std::cout << "Too high!" << std::endl;
        }
        else if (guess < num)
        {
            std::cout << "Too low!" << std::endl;
        }
        else
        {
            std::cout << "You got it! It took you " << tries << " tries." << std::endl;
        }
        
    } while (guess != num);
    

    return 0;
}