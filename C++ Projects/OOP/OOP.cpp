#include <iostream>
using namespace std;

class Employee {
public:
    string Name;
    string Company;
    int Age;

    /**
     * @brief Prints the employee's details to the console
     *
     * Prints the employee's name, company and age to the console in a formatted manner
     */
    void print() {
        cout << "Name: " << Name << endl;
        cout << "Company: " << Company << endl;
        cout << "Age: " << Age << endl;
    }
};
/**
 * @brief The main entry point of the program
 *
 * Creates an Employee object, sets its details and prints them to the console using the print() method
 *
 * @return 0 on successful execution
 */
int main() {
    Employee employee1;
    employee1.Name = "John Doe";
    employee1.Company = "ABC Company";
    employee1.Age = 30;

    Employee employee2;
    employee2.Name = "Jane Doe";
    employee2.Company = "XYZ Company";
    employee2.Age = 25;

    employee1.print();
    employee2.print();

    return 0;
}