#include <iostream>
#include <cmath>

int main() {
    
    // switch = alternative to using multiple if statements
    //          allows for multiple conditions to be tested
    //          instead of testing one condition at a time
    //          if (month == 1) { ... } else if (month == 2) { ... } etc. would be redundant in this case

    // switch is similar to a series of if statements

    int month;

    std::cout << "Enter the number of the month: ";
    std::cin >> month;

    switch (month) {
        case 1:
            std::cout << "It is January" << std::endl;
            break;
        case 2:
            std::cout << "It is February" << std::endl;
            break;
        case 3:
            std::cout << "It is March" << std::endl;
            break; 
        case 4:
            std::cout << "It is April" << std::endl;
            break;
        case 5:
            std::cout << "It is May" << std::endl;
            break;
        case 6:
            std::cout << "It is June" << std::endl;
            break;
        case 7:
            std::cout << "It is July" << std::endl;
            break;
        case 8:
            std::cout << "It is August" << std::endl;
            break;
        case 9:
            std::cout << "It is September" << std::endl;
            break;
        case 10:
            std::cout << "It is October" << std::endl;
            break;
        case 11:
            std::cout << "It is November" << std::endl;
            break;
        case 12:
            std::cout << "It is December" << std::endl;
            break;
        default:
            std::cout << "Invalid month number" << std::endl;
            break;
    }

    return 0;
}