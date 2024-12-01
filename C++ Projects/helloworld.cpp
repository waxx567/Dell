#include <iostream>
#include <iomanip>

void showBalance(double balance);
double deposit();
double withdraw(double balance);

/**
 * @brief Main entry point of the program
 *
 * This function creates a bank account program. It asks the user to make a choice
 * from the menu and performs the chosen action. The user can deposit money, withdraw
 * money, show the balance or exit the program.
 *
 * @return 0 on success
 */
int main() {

    double balance = 0;
    int choice = 0;

    do
    {
    std::cout << "Enter your choice: " << std::endl;
    std::cout << "1. Deposit" << std::endl;
    std::cout << "2. Withdraw" << std::endl;
    std::cout << "3. Show balance" << std::endl;
    std::cout << "4. Exit" << std::endl;

    std::cout << "Choice: ";
    std::cin >> choice;

    if (choice != 1 || choice != 2 || choice != 3 || choice != 4)
    {
        std::cout << "Invalid choice" << std::endl;
        break;
    }    

    // Clear the input buffer if the user enters invalid input
    // std::cin.clear();
    // fflush(stdin);

    switch (choice) {
        case 1:
            balance += deposit();
            showBalance(balance);
            break;
        case 2:
            balance -= withdraw(balance);
            showBalance(balance);
            break;
        case 3:
            showBalance(balance);
            break;
        case 4:
            std::cout << "Goodbye!" << std::endl;
            break;
        default:
            std::cout << "Invalid choice" << std::endl;
            break;
        }
    } while (choice != 4);

    return 0;
}

// Displays the current balance to the user
void showBalance(double balance) {
    std::cout << "Your balance is ZAR " << std::setprecision(2) << std::fixed << balance << std::endl;
}

// Prompts the user to enter an amount to deposit and returns that amount.
double deposit() {
    double amount;
    std::cout << "Enter the amount to deposit: ";
    std::cin >> amount;

    if (amount > 0)
    {
        return amount;
    }
    else
    {
        std::cout << "Invalid amount" << std::endl;
        return 0;
    }
}

// Prompts the user to enter an amount to withdraw, checks if the amount is less than or equal to the current balance, and returns the withdrawn amount. If the amount is greater than the balance, it displays an error message and returns 0.
double withdraw(double balance) {
    double amount;
    std::cout << "Enter the amount to withdraw: ";
    std::cin >> amount;

    if (amount > balance)
    {
        std::cout << "Insufficient funds" << std::endl;
        return 0;
    }
    else if (amount > 0)
    {
        return amount;
    }
    else
    {
        std::cout << "Invalid amount" << std::endl;
        return 0;
    }
}