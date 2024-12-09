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

    Employee(string name, string company, int age) {
        Name = name;
        Company = company;
        Age = age;
    }
};
/**
 * @brief The main entry point of the program
 *
 * Creates two Employee objects, sets their details and prints them to the console using the print() method
 *
 * @return 0 on successful execution
 */
int main() {

    Employee employee1 = Employee("John Doe", "ABC Company", 30);
    employee1.print();

    Employee employee2 = Employee("Jane Doe", "XYZ Company", 25);
    employee2.print();

    return 0;
}