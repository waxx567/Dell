#include <iostream>

double getTotal(double prices[], int size);

/**
 * @brief The main entry point of the program
 *
 * @details This function contains the main logic of the program.
 *          It creates an array of prices, calculates the total
 *          and prints it to the console.
 */
int main() {

    // pass an array to a function
    double prices[] = {10.99, 12.50, 9.99, 7.50, 6.00};
    int size = sizeof(prices) / sizeof(prices[0]);
    double total = getTotal(prices, size);

    std::cout << "Total: $" << total << std::endl;

    return 0;
}

/**
 * @brief Calculates the total of an array of prices
 *
 * @param prices the array of prices
 *
 * @return the total of the prices
 */
double getTotal(double prices[], int size) {
    double total = 0;
    for (int i = 0; i < size; i++) {
        total += prices[i];
    }
    return total;
}