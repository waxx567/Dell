// Prints out how long (in years) it takes a population of llamas to reach a given size

#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{

    // TODO: Prompt for start size
    // Keep asking until input is 9 or over
    int start_size;
    do
    {
        start_size = get_int("Start size: ");
    }
    while (start_size < 9);

    // Prompt for end size
    // Keep asking until input is greater than the start size
    int end_size;
    do
    {
        end_size = get_int("End size: ");
    }
    while (end_size < start_size);

    // TODO: Calculate number of years until we reach threshold
    // Variable to use for updating formula inside loop
    int calc = start_size;

    // Variable to store years total
    int years = 0;

    // Loop from start to end subtracting deaths from births and adding to the years total
    while (calc < end_size)
    {
        calc = calc + ((calc / 3) - (calc / 4));
        years++;
    }

    // TODO: Print number of years
    // Print answer
    printf("Years: %i\n", years);
}