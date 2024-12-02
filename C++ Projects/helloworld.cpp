#include <iostream>

int searchArray(std::string array[], int size, std::string element);

/**
 * @brief The main entry point of the program
 *
 * @details This function asks the user to input their favorite food and checks if it is present in the array.
 *          If the food is present in the array, it outputs the food.
 *          Otherwise, it tells the user that the food was not found in the array.
 */
int main() {

    std::string foods[] = {"apple", "banana", "cherry", "date", "elderberry"};
    int size = sizeof(foods) / sizeof(std::string);
    int index;
    std::string myFood;

    std::cout << "Enter your favorite food: ";
    std::cin >> myFood;

    index = searchArray(foods, size, myFood);

    if (index != -1) {
        std::cout << "Your favorite food is at index " << index << ": " << foods[index] << std::endl;
    }
    else {
        std::cout << "Your favorite food " << myFood << " is not in the list" << std::endl;
    }

    return 0;
}

/**
 * @brief Searches an array for an element and returns the index of the element if found
 *
 * @param array the array to search
 * @param size the size of the array
 * @param element the element to search for
 *
 * @return the index of the element if found, -1 otherwise
 */
int searchArray(std::string array[], int size, std::string element) {

    for (int i = 0; i < size; i++) {
        if (array[i] == element) {
            return i;
        }
    }

    return -1;
}