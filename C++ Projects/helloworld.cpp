#include <iostream>

int main() {

    // nested loops = a loop within a loop
    // outer loop = the loop that contains the inner loop
    // inner loop = the loop that is contained within the outer loop

    // print a rectangle with user input
    int rows;
    int columns;
    char symbol;

    std::cout << "Enter the number of rows: ";
    std::cin >> rows;

    std::cout << "Enter the number of columns: ";
    std::cin >> columns;

    std::cout << "Enter the symbol: ";
    std::cin >> symbol;

    for (int i = 1; i <= rows; i++) {
        for (int j = 1; j <= columns; j++) {
            std::cout << symbol;
        }
        std::cout << std::endl;
    }

    return 0;
}