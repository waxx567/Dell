#include <iostream>

int main() {

    // sort an array
    // bubble sort
    int arr[] = {5, 2, 8, 1, 9, 3, 6, 4, 7};
    int size = sizeof(arr) / sizeof(arr[0]);

    for (int element : arr) {
        std::cout << element << " ";
    }

    return 0;
}