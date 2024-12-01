#include <iostream>

char getUserChoice();
char getComputerChoice();
void showChoice(char choice);
void chooseWinner(char player, char computer);

/**
 * Main entry point of the Rock Paper Scissors game.
 *
 * This function prompts the user for input, generates a random choice
 * for the computer, shows the choices and determines the winner.
 */
int main() {
    char player;
    char computer;

    player = getUserChoice();
    std::cout << "Your choice: ";
    showChoice(player);
    // computer = getComputerChoice();
    // showChoice(computer);
    // chooseWinner(player, computer);

    return 0;
}

/**
 * Prompts the user to enter their choice for the Rock Paper Scissors game.
 *
 * This function shows the game title and repeatedly prompts the user for
 * their choice until the user enters a valid choice. Valid choices are 'r',
 * 'p', 's' for rock, paper and scissors respectively.
 *
 * @return The user's choice as a character.
 */
char getUserChoice() {
    char player;
    std::cout << "****Rock Paper Scissors Game****" << std::endl;

    do
    {
        std::cout << "Enter your choice: " << std::endl;
        std::cout << "'r' for rock" << std::endl;
        std::cout << "'p' for paper" << std::endl;
        std::cout << "'s' for scissors" << std::endl;
        std::cin >> player;        
    } while (player != 'r' && player != 'p' && player != 's');

    return 0;
}
char getComputerChoice() {
    return 0;
}
void showChoice(char choice) {
    switch (choice)
    {
    case 'r':
        std::cout << "Rock" << std::endl;
        break;
    case 'p':
        std::cout << "Paper" << std::endl;
        break;
    case 's':
        std::cout << "Scissors" << std::endl;
        break;
    }
}
void chooseWinner(char player, char computer) {
    return;
}