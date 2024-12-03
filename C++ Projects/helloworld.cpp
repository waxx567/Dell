#include <iostream>

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
    
    return 0;
}

void drawBoard(char *spaces) {
    // draw the tic-tac-toe board
    std::cout << "   |   |   " << std::endl;
    std::cout << " " << spaces[0] << " | " << spaces[1] << " | " << spaces[2] << std::endl;
    std::cout << "___|___|___" << std::endl;
    std::cout << "   |   |   " << std::endl;
    std::cout << " " << spaces[3] << " | " << spaces[4] << " | " << spaces[5] << std::endl;
    std::cout << "___|___|___" << std::endl;
    std::cout << "   |   |   " << std::endl;
    std::cout << " " << spaces[6] << " | " << spaces[7] << " | " << spaces[8] << std::endl;
    std::cout << "   |   |   " << std::endl;


}

void playerMove(char *spaces, char player) {
    // get the player's move
}

void computerMove(char *spaces, char computer) {
    // get the computer's move    
}

bool checkWinner(char *spaces, char player, char computer) {
    // check if there is a winner
    return 0;
}

bool checkTie(char *spaces) {
    // check if there is a tie
    return 0;
}