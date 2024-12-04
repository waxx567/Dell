#include <iostream>
#include <ctime>

void drawBoard(char *spaces);
void playerMove(char *spaces, char player);
void computerMove(char *spaces, char computer);
bool checkWinner(char *spaces, char player, char computer);
bool checkTie(char *spaces);

int main() {

    // create a tic-toc-toe game
    char spaces[9] = {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '};
    char player = 'X';
    char computer = 'O';
    bool running = true;

    drawBoard(spaces);

    while (running) {
        playerMove(spaces, player);
        drawBoard(spaces);

        computerMove(spaces, computer);
        drawBoard(spaces);
    }
    
    return 0;
}

/**
 * @brief Draw the Tic-Tac-Toe board
 *
 * This function prints out the Tic-Tac-Toe board to the console.
 *
 * @param spaces The array of characters representing the spaces on the board
 */
void drawBoard(char *spaces) {
    std::cout << std::endl;
    std::cout << "     |     |     " << std::endl;
    std::cout << "  " << spaces[0] << "  |  " << spaces[1] << "  |  " << spaces[2] << std::endl;
    std::cout << "_____|_____|_____" << std::endl;
    std::cout << "     |     |     " << std::endl;
    std::cout << "  " << spaces[3] << "  |  " << spaces[4] << "  |  " << spaces[5] << std::endl;
    std::cout << "_____|_____|_____" << std::endl;
    std::cout << "     |     |     " << std::endl;
    std::cout << "  " << spaces[6] << "  |  " << spaces[7] << "  |  " << spaces[8] << std::endl;
    std::cout << "     |     |     " << std::endl;
    std::cout << std::endl;
}

/**
 * @brief Allows the player to make a move on the Tic-Tac-Toe board.
 *
 * This function prompts the player to enter a number corresponding to 
 * a position on the Tic-Tac-Toe board, and updates the board with the 
 * player's symbol if the selected position is empty.
 *
 * @param spaces The array representing the current state of the board.
 * @param player The character symbol representing the player ('X' or 'O').
 */
void playerMove(char *spaces, char player) {
    int number;

    do
    {
        std::cout << "Enter a number (1-9): ";
        std::cin >> number;
        number--;

        if (spaces[number] == ' ') {
            spaces[number] = player;
        }
    } while (number < 1 || number > 9);    
}

void computerMove(char *spaces, char computer) {
    // get the computer's move
    int number;
    srand(time(0));
}

bool checkWinner(char *spaces, char player, char computer) {
    // check if there is a winner
    return 0;
}

bool checkTie(char *spaces) {
    // check if there is a tie
    return 0;
}