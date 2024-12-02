#include <iostream>
#include <string>

/**
 * @brief A simple program that asks the user for five bike names and
 *        prints them out afterwards.
 *
 * @details This program does not do any error checking on the input. It
 *          simply assumes that the user will enter five valid bike names.
 */
int main() {

    // the problem is the empty string will be added to the array if the user enters fewer than 5

    std::string bikes[5];
    int size = sizeof(bikes) / sizeof(bikes[0]);
    std::string temp;

    for (int i = 0; i < size; i++) {
        std::cout << "Enter a bike or 'q' to quit #" << i + 1 << ": ";
        std::getline(std::cin, temp);

        if (temp == "q") {
            break;
        }
        else
        {
            bikes[i] = temp;
        }
    }

    std::cout << "Your bikes are: " << std::endl;

    for (std::string bike : bikes) {
        std::cout << bike << std::endl;
    }

    return 0;
}