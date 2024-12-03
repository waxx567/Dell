#include <iostream>
#include <string>

// test credit card account numbers

int getDigit(const int number);
int sumOddDigits(const std::string number);
int sumEvenDigits(const std::string number);

int main() {

    // Luhn Algorithm
    // 1. Double every second digit starting from right to left. If the doubled result is 2 digits, split them up.
    // 2. Add all the digits together.
    // 3. Add all odd numbered digits from left to right of the original number.
    // 4 Sum the results from steps 2 and 3.
    // 5. If the sum from step 4 is divisible by 10, the number is valid.

    std::string cardNumber;
    int result;

    std::cout << "Enter your credit card number: ";
    std::getline(std::cin, cardNumber);

    result = sumOddDigits(cardNumber) + sumEvenDigits(cardNumber);

    return 0;
}

int getDigit(const int number) {
    
    return number % 10 + (number / 10 % 10);
}

int sumOddDigits(const std::string cardNumber) {
    return 0;
}   

int sumEvenDigits(const std::string cardNumber) {   
    
    int sum = 0;

    for (int i = cardNumber.size() - 2; i >= 0; i-=2) {
        sum += getDigit(cardNumber[i] - '0')*2;
    }
    
    return sum;
}
