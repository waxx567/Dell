#include <iostream>
using std::string;
using std::cout;
using std::endl;

class Employee {
private:
    string Name;
    string Company;
    int Age;

public:
    void setName(string name) {
        Name = name;
    }
    string getName() {
        return Name;
    }
    void setCompany(string company) {
        Company = company;
    }
    string getCompany() {
        return Company;
    }
    void setAge(int age) {
        Age = age;
    }
    int getAge() {
        return Age;
    }
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

    /**
     * @brief Constructor to create an Employee object
     *
     * @param name The name of the employee
     * @param company The company the employee works for
     * @param age The age of the employee
     *
     * @details Sets the Name, Company and Age of the Employee object
     */
    Employee(string name, string company, int age) {
        Name = name;
        Company = company;
        Age = age;
    }
};

/**
 * @brief The main entry point of the program
 *
 * This function creates two Employee objects with specified names, companies, and ages.
 * It then prints their details to the console using the print() method of the Employee class.
 *
 * @return 0 on successful execution
 */
int main() {

    Employee employee1 = Employee("John Doe", "ABC Company", 30);
    employee1.print();

    Employee employee2 = Employee("Jane Doe", "XYZ Company", 25);
    employee2.print();

    employee1.setAge(31);
    cout << employee1.getName() << " is " << employee1.getAge() << " years old" << endl;

    return 0;
}