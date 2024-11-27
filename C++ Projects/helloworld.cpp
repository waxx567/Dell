#include <iostream> 

int main() {
    
    // int is a whole number
    int weeks = 6;
    int days = 7.5; // would output 7 (the value is truncated)

    // double is a decimal
    double pi = 3.14159;

    // char is a character
    char grade = 'A';
    char currency = '$';
    // If you tried
    char initials = 'WPM'; // you'd get an overflow error and only output the last character - M in this case

    //bool is a boolean
    bool power = true; // if the power is on

    // string is a collection of characters
    std::string name = "Wayne";

    return 0;
}