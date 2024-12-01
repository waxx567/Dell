#include <iostream>
#include <ctime>

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
    std::cout << "You chose: ";
    showChoice(player);

    computer = getComputerChoice();
    std::cout << "The computer chose: ";
    showChoice(computer);
    
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

    return player;
}
/**
 * Generates a random choice for the computer in the Rock Paper Scissors game.
 *
 * This function uses the random number generator to select a number between
 * 1 and 3, which corresponds to 'r' (rock), 'p' (paper), or 's' (scissors).
 *
 * @return The computer's choice as a character ('r', 'p', or 's').
 */
char getComputerChoice() {

    srand(time(0));

    int num = rand() % 3 + 1;

    switch (num)
    {
    case 1: 
        return 'r';
    case 2:
        return 'p';
    case 3:
        return 's';
    }

    return 0;
}
/**
 * Displays the textual representation of the player's or computer's choice.
 *
 * This function takes a character representing the choice ('r', 'p', 's')
 * and prints the corresponding string ("Rock", "Paper", "Scissors") to the console.
 *
 * @param choice The character representing the choice to display.
 */
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