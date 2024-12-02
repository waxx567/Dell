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

    // change the for loop to use the bikes array and check for empty strings
    for (int i = 0; !bikes[i].empty(); i++) {
        std::cout << bikes[i] << std::endl;
    }

    return 0;
}