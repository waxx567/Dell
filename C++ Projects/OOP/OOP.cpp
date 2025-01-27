#include <iostream>
using std::string;
using std::cout;
using std::endl;

//The AbstractEmployee class is an abstract base class that cannot be instantiated on its own.
// It has one pure virtual method:
// AskForPromotion(): This method is declared but not defined, and must be implemented by any non-abstract derived classes. It is intended to provide a way for employees to ask for promotions, but the implementation details are left to the derived classes.
class AbstractEmployee {
    virtual void AskForPromotion() = 0;
};
// setName(string name): Sets the name of the employee.
// getName(): Returns the name of the employee.
// setCompany(string company): Sets the company of the employee.
// getCompany(): Returns the company of the employee.
// setAge(int age): Sets the age of the employee, but only if the age is 18 or above.
// getAge(): Returns the age of the employee.
// print(): Prints the employee's details (name, company, age) to the console.
// Employee(string name, string company, int age): Constructor to create an Employee object. It sets the Name, Company, and Age of the Employee object.
// AskForPromotion(): If the employee's age is greater than 30, it prints that the employee got promoted. Otherwise, it prints that the employee didn't get promoted.
// Note: The Employee class is a subclass of the AbstractEmployee class. The AbstractEmployee class has a pure virtual method AskForPromotion() which must be implemented by any non-abstract derived classes.
// The Employee class is a simple implementation of an employee. It has private member variables for the name, company, and age of the employee. It also has getter and setter methods for these variables. The print() method is used to print the employee's details to the console. The AskForPromotion() method checks the employee's age and prints a message based on whether the employee got promoted or not.
// The Employee class also has a constructor that takes in the name, company, and age of the employee and sets these values in the object.
// The class is also a subclass of the AbstractEmployee class, which means it inherits the pure virtual method AskForPromotion() from the base class.
class Employee:AbstractEmployee {
private:
    string Company;
    int Age;
protected:
    string Name;
public:
    /**
     * @brief Sets the name of the employee
     *
     * @param name The name to be set for the employee
     */
    void setName(string name) {
        Name = name;
    }
    /**
     * @brief Returns the name of the employee
     *
     * @return The name of the employee
     */
    string getName() {
        return Name;
    }
    /**
     * @brief Sets the company of the employee
     *
     * @param company The company to be set for the employee
     */
    void setCompany(string company) {
        Company = company;
    }
    /**
     * @brief Returns the company of the employee
     *
     * @return The company of the employee
     */
    string getCompany() {
        return Company;
    }
    /**
     * @brief Sets the age of the employee
     *
     * @param age The age to be set for the employee
     *
     * @details Only sets the age if the age is 18 or above
     */
    void setAge(int age) {
        if(age >= 18)
        Age = age;
    }
    /**
     * @brief Returns the age of the employee
     *
     * @return The age of the employee
     */
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
    /**
     * @brief Determines if the employee is eligible for a promotion
     *
     * Checks the age of the employee and prints a message indicating
     * whether the employee got promoted based on the condition that
     * the age is greater than 30.
     */
    void AskForPromotion() {
        if(Age > 30)
        cout << Name << " got promoted" << endl;
        else
        cout << Name << " didn't get promoted" << endl;
    }
    /**
     * @brief Simulates the employee working
     *
     * Prints a message to the console indicating that the employee is working
     */
    virtual void Work() {
        cout << Name << " is working" << endl;
    }
};
// The Developer class is a subclass (child) of the Employee (parent) class.
// Class Overview 
// The Developer class is a subclass of the Employee class, inheriting its properties and methods. It adds a FavoriteProgrammingLanguage attribute and three methods specific to developers.
// Class Methods
// Constructor (Developer): Initializes a Developer object with a name, company, age, and favorite programming language, inheriting name, company, and age from the Employee class.
// FixBug: Simulates a developer fixing a bug by printing a message to the console indicating the developer's name and favorite programming language used.
// Work: Simulates a developer working by printing a message to the console indicating the developer's name and favorite programming language used.
class Developer: public Employee {
public:
    string FavoriteProgrammingLanguage;
    /**
     * @brief Constructor to create a Developer object
     *
     * @param name The name of the developer
     * @param company The company the developer works for
     * @param age The age of the developer
     * @param favoriteProgrammingLanguage The developer's favorite programming language
     *
     * @details Initializes a Developer object by setting the name, company, age, and favorite programming language. Inherits name, company, and age initialization from the Employee class.
     */
    Developer(string name, string company, int age, string favoriteProgrammingLanguage) : Employee(name, company, age) {
        FavoriteProgrammingLanguage = favoriteProgrammingLanguage;
    }
    /**
     * @brief Simulates the developer fixing a bug using their favorite programming language
     *
     * Prints a message to the console indicating that the developer fixed a bug using their favorite programming language
     */
    void FixBug() {
        cout << Name << " fixed a bug using " << FavoriteProgrammingLanguage << endl;
    }
    /**
     * @brief Simulates the developer working
     *
     * Prints a message to the console indicating that the developer is working
     */
    void Work() {
        cout << Name << " is coding" << " using " << FavoriteProgrammingLanguage << endl;
    }
};
// The Teacher class is a subclass (child) of the Employee (parent) class.
// Class Overview: T
// he Teacher class is a subclass of the Employee class, inheriting its properties and methods. It adds a Subject attribute and three methods specific to teachers.
// Class Methods:
// PrepareLesson(): Simulates a teacher preparing a lesson on their subject by printing a message to the console.
// Teacher(string name, string company, int age, string subject): Initializes a Teacher object by setting the name, company, age, and subject, inheriting name, company, and age initialization from the Employee class.
// Work(): Simulates a teacher working by printing a message to the console indicating that the teacher is teaching their subject.
// Note: The Name variable used in the PrepareLesson() and Work() methods is inherited from the Employee class.
class Teacher: public Employee {
public:
    string Subject;
    /**
     * @brief Simulates the teacher preparing a lesson on their subject
     *
     * Prints a message to the console indicating that the teacher is preparing a lesson on their subject
     */
    void PrepareLesson() {
        cout << Name << " is preparing a lesson on " << Subject << endl;
    }
    /**
     * @brief Constructor to create a Teacher object
     *
     * @param name The name of the teacher
     * @param company The company the teacher works for
     * @param age The age of the teacher
     * @param subject The subject the teacher will be teaching
     *
     * @details Initializes a Teacher object by setting the name, company, age, and subject. Inherits name, company, and age initialization from the Employee class.
     */
    Teacher(string name, string company, int age, string subject) : Employee(name, company, age) {
        Subject = subject;
    }
    /**
     * @brief Simulates the teacher working
     *
     * Prints a message to the console indicating that the teacher is teaching
     */
    void Work() {
        cout << Name << " is teaching" << " " << Subject << endl;
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

    Developer developer1 = Developer("John Doe", "ABC Company", 31, "C++");

    Teacher teacher1 = Teacher("Jane Doe", "XYZ Company", 25, "Math");
    
    Employee *e1 = &developer1;
    Employee *e2 = &teacher1;

    e1->Work();

    e2->Work();

    return 0;
}