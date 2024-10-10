// Prints out how long (in years) it takes a population of llamas to reach a given size

#include <cs50.h>
#include <stdio.h>
#include <math.h>

// Calls function to get start population amount from user
int start_ask(void);

// Calls function to get end population amount from user
int end_ask(int i);

int main(void)
{
    int start_size, end_size, answer = 0;
    // TODO: Prompt for start size
    // User inputs how many llamas there were at the start
    start_size = start_ask();
    printf("start size (checks function): %i\n", start_size);

    // TODO: Prompt for end size
    // User inputs how many llamas there were at the end
    end_size = end_ask(start_size);
    printf("end size (checks function): %i\n", end_size);

    // TODO: Calculate number of years until we reach threshold
    // The difference between the two inputs is how many llamas have been added in total
    float llamas_added = end_size - start_size;
    printf("llamas added (checks subtraction): %.2f\n", llamas_added);

    // TODO: Print number of years
    // Amount of llamas born in a year
    double born = (double) start_size / 3;
    printf("born (checks division): %.2f\n", born);

    // Amount of llamas that die in a year
    double died = (double) start_size / 4;
    printf("died (checks division): %.2f\n", died);

    // Calculates how many llamas survive in a year
    float yearly_gain = born - died;
    printf("yearly gain (checks subtraction): %.2f\n", yearly_gain);

    // Calculates how many years it would take the herd to reach the end size
    float years = llamas_added / yearly_gain;
    answer = round(years);
    printf("Years: %d\n", answer);
}

// Function to get start population amount from user as long as amount is 9 or over
int start_ask(void)
{
    int s;
    do
    {
        s = get_int("Start size: ");
    }
    while (s < 9);
    return s;
}

// Function to get end population amount from user as long as amount is greater than or equal to the start size
int end_ask(int i)
{
    int e;
    printf("int i (checks function input): %i\n", i);
    do
    {
        e = get_int("End size: ");
    }
    while (e < i);
    return e;
}