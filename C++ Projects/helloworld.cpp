#include <iostream>

int main() {
    
    // dynamic memory allocation = the process of creating memory on the heap
    // whenever you use the 'new' operator, you should also use the 'delete' operator
    
    char *pGrades = NULL;
    int size;

    std::cout << "Enter the number of students: ";
    std::cin >> size;

    pGrades = new char[size];

    for (int i = 0; i < size; i++) {
        std::cout << "Enter the grade for student " << i + 1 << ": ";
        std::cin >> pGrades[i];
    }

    for (int i = 0; i < size; i++) {
        std::cout << "Grade for student " << i + 1 << ": " << pGrades[i] << std::endl;
    }

    delete[] pGrades;

    return 0;
}