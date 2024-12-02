#include <iostream>

int searchArray(int array[], int size, int element);

/**
 * @brief The main entry point of the program
 *
 * @details This function asks the user to input a number and checks if it is present in the array.
 *          If the number is present in the array, it outputs the index of the number.
 *          Otherwise, it tells the user that the number was not found in the array.
 */
int main() {

    int numbers[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int size = sizeof(numbers) / sizeof(int);
    int index;
    int myNum;

    std::cout << "Enter a number: ";
    std::cin >> myNum;

    index = searchArray(numbers, size, myNum);

    if (index != -1) {
        std::cout << "The number " << myNum << " is at index " << index << std::endl;
    }
    else {
        std::cout << "The number " << myNum << " was not found in the array" << std::endl;
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
int searchArray(int array[], int size, int element) {

    for (int i = 0; i < size; i++) {
        if (array[i] == element) {
            return i;
        }
    }

    return -1;
}