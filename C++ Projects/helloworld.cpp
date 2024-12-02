#include <iostream>

/**
 * @brief The main entry point of the program
 *
 * @details This function contains an array of questions and an array of options
 *          for each question. It also contains an array of the correct answers
 *          for each question. The function iterates over the questions and options
 *          and prints them to the console, formatting them with asterisks.
 *
 * @return 0 on successful execution
 */
int main() {

    std::string questions[] = {
        "1. What is the capital of France?",
        "2. What is the largest planet in our solar system?",
        "3. What is the smallest planet in our solar system?",
        "4. What is the largest mammal in the world?"
    };

    std::string options[] = {
        "a. Rome", "b. London", "c. Paris", "d. Madrid",
        "a. Jupiter", "b. Saturn", "c. Neptune", "d. Earth",
        "a. Earth", "b. Venus", "c. Mercury", "d. Mars",
        "a. Elephant", "b. Whale", "c. Lion", "d. Crocodile"
    };

    char answerKey[] = {'c', 'a', 'c', 'b'};

    int size = sizeof(questions) / sizeof(questions[0]);
    char guess;
    int score;

    for (int i = 0; i < size; i++) {
        std::cout << "***************************************************" << std::endl;
        std::cout << questions[i] << std::endl;
        std::cout << "***************************************************" << std::endl;

        for (int j = i * 4; j < (i * 4 + 4); j++) {
            std::cout << options[j] << std::endl;
        }
    }

    return 0;
}