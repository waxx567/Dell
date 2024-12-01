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
    computer = getComputerChoice();
    showChoice(player);
    showChoice(computer);
    chooseWinner(player, computer);

    return 0;
}


char getUserChoice() {
    char player;
    std::cout << "****Rock Paper Scissors Game****" << std::endl;
    std::cout << "'r' for rock, 'p' for paper, 's' for scissors" << std::endl;    
    std::cin >> player;

    std::cout << "You choose: " << player << std::endl;
    
    return 0;
}
char getComputerChoice() {
    return 0;
}
void showChoice(char choice) {
    return;
}
void chooseWinner(char player, char computer) {
    return;
}