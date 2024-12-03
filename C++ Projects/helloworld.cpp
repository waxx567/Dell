#include <iostream>
#include <string>

// Program to test credit card account numbers
    // Luhn Algorithm
    // 1. Double every second digit starting from right to left. If the doubled result is 2 digits, split them up.
    // 2. Add all the digits together.
    // 3. Add all odd numbered digits from left to right of the original number.
    // 4 Sum the results from steps 2 and 3.
    // 5. If the sum from step 4 is divisible by 10, the number is valid.

int getDigit(const int number);
int sumOddDigits(const std::string number);
int sumEvenDigits(const std::string number);

/**
 * The main entry point of the program.
 *
 * This function prompts the user for a credit card number, checks the number
 * using the Luhn Algorithm, and displays whether the number is valid or not.
 */
int main() {

    std::string cardNumber;
    int result;

    std::cout << "Enter your credit card number: ";
    std::getline(std::cin, cardNumber);

    result = sumOddDigits(cardNumber) + sumEvenDigits(cardNumber);

    if (result % 10 == 0) {
        std::cout << "The credit card number is valid." << std::endl;
    }
    else {
        std::cout << "The credit card number is not valid." << std::endl;
    }

    return 0;
}

/**
 * @brief Returns the sum of the digits of the given number.
 *
 * This is used in the Luhn Algorithm to calculate the sum of the digits of
 * every second digit, starting from the right, in the card number.
 *
 * @param number The number to get the sum of the digits from.
 *
 * @return The sum of the digits of the given number.
 */
int getDigit(const int number) {
    
    return number % 10 + (number / 10 % 10);
}

/**
 * @brief Calculates the sum of the digits of every second digit, 
 *        starting from the right, in the card number.
 *
 * @param cardNumber The credit card number as a string.
 * @return The sum of processed digits.
 */
int sumOddDigits(const std::string cardNumber) {
    
    int sum = 0;

    for (int i = cardNumber.size() - 1; i >= 0; i-=2) {
        sum += getDigit(cardNumber[i] - '0');
    }
    
    return sum;
}   

/**
 * @brief Calculates the sum of the digits of every second digit, 
 *        starting from the second-to-last, in the card number.
 *
 * @param cardNumber The credit card number as a string.
 * @return The sum of processed digits, where each digit is doubled.
 */
int sumEvenDigits(const std::string cardNumber) {   
    
    int sum = 0;

    for (int i = cardNumber.size() - 2; i >= 0; i-=2) {
        sum += getDigit(cardNumber[i] - '0')*2;
    }
    
    return sum;
}
