#include <iostream>

int main() {
    
    // calculate how many questions a student gets right
    // out of the total number of questions

    int correct = 8;
    int questions = 10;
    // so you can explicitly cast questions as a double
    double percent = correct / (double) questions * 100;

    std::cout << percent << "%"; // outputs 80%

    return 0;
}