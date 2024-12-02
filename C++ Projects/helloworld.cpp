#include <iostream>

void sortArray(int arr[], int size);

/**
 * @brief Entry point of the program
 *
 * This program sorts an array of integers in ascending order using the
 * bubble sort algorithm, and prints the sorted array to the console.
 *
 * @return 0 on success
 */
int main() {

    int array[] = {5, 2, 8, 1, 9, 3, 6, 4, 7};
    int size = sizeof(array) / sizeof(array[0]);

    sortArray(array, size);

    for (int element : array) {
        std::cout << element << " ";
    }

    return 0;
}

/**
 * @brief Sorts an array of integers in ascending order using the
 *        bubble sort algorithm.
 *
 * @param arr the array to be sorted
 * @param size the size of the array
 */
void sortArray(int arr[], int size) {

    int temp;

    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}