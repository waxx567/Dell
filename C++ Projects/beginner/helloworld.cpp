#include <iostream>

// inheritance
// another example

class Shape {
    public:
    double area;
    double volume;
};
class Cube : public Shape {
    public:
    double side;   
    /**
     * @brief Constructor to create a cube with given side length
     *
     * @param side The length of each side of the cube
     */
    Cube(double side) {
        this->side = side;
        this->area = 6 * side * side;
        this->volume = side * side * side;
    } 
};
class Sphere : public Shape {
    public:
    double radius;
    /**
     * @brief Constructor to create a sphere with given radius
     *
     * @param radius The radius of the sphere
     *
     * @details Calculates the area and volume of the sphere based on the radius
     */
    Sphere(double radius) {
        this->radius = radius;
        this->area = 4 * 3.14159 * (radius * radius);
        this->volume = (4 / 3.0) * 3.14159 * (radius * radius * radius);
    }
};

/**
 * @brief The main entry point of the program
 *
 * This function creates a Cube and a Sphere object with a side length and radius of 10, respectively.
 * It calculates their areas and volumes, and outputs the results to the console.
 *
 * @return 0 on successful execution
 */
int main() {

    Cube cube(10);
    Sphere sphere(10);

    std::cout << "The area of the cube is: " << cube.area<< "cm^2" << std::endl;
    std::cout << "The volume of the cube is: " << cube.volume << "cm^3" << std::endl;
    std::cout << "The area of the sphere is: " << sphere.area << "cm^2" << std::endl;
    std::cout << "The volume of the sphere is: " << sphere.volume << "cm^3" << std::endl;

    return 0;
}