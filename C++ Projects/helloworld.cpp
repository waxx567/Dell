#include <iostream>

/**
 * @brief The main entry point of the program
 *
 * @details This function contains the game's logic and user interface. It
 *          prompts the user with a series of questions, and then displays
 *          the results of how many questions were answered correctly.
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

        std::cin >> guess;
        guess = tolower(guess);

        if (guess == answerKey[i]) {
            std::cout << "Correct!" << std::endl;
            score++;
        }
        else {
            std::cout << "Incorrect!" << std::endl;
            std::cout << "The correct answer is: " << answerKey[i] << std::endl;
        }
    }
    std::cout << "***************************************************" << std::endl;
    std::cout << "*                   RESULTS                       *" << std::endl;
    std::cout << "***************************************************" << std::endl;
    std::cout << "You got " << score << " out of " << size << " questions correct!" << std::endl;
    std::cout << "Score: " << (score/size * 100) << std::endl;

    return 0;
}