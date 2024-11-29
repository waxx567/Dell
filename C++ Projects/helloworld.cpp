#include <iostream>

int main() {
    
    // calculate how many questions a student gets right
    // out of the total number of questions

    int correct = 8;
    int questions = 10;
    double percent = correct / questions * 100;

    std::cout << percent << "%"; // outputs 0% because the int data type truncates the value

    // this won't work because the output is a double
    // std::cout << correct / questions * 100 << "%";

    return 0;
}