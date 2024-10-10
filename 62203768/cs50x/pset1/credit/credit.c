#include <cs50.h>
#include <stdio.h>
#include <string.h>

long get_number(void);

int main(void)
{

    // Store from user input for first check
    long n = get_number();

    // Store from user input for second check
    long n1 = n;

    // To manipulate last digit and every second one from there
    int set1 = 0;

    // To manipulate second last digit and every second one from there
    int set2 = 0;

    // Variables to store totals
    int x = 0;
    int y = 0;

    // Save as a string for length check
    char str[256];
    sprintf(str, "%ld", n1);

    // Checksum loop through long n
    while (n > 0)
    {

        // Add last digit off long n to set1
        set1 = n % 10;

        // Slice that digit off
        n = n / 10;

        // Store in x
        x = x + set1;

        // Add last (originally second last) digit off long n to set2
        set2 = n % 10;

        // Slice that digit off
        n = n / 10;

        // Places in set3 for manipulation
        // Multiplies set2 by 2
        int set3 = set2 * 2;

        // If this value greater than 10, the two digits must be added together
        if (set3 >= 10)
        {

            // Slice the last digit off and add the 1 (not 10)
            set3 = (set3 % 10) + 1;

            // Assign to set2
            set2 = set3;
        }

        // If this value less than 9, the doubled value is fine as is
        else
        {
            set2 = set3;
        }

        // Store in y
        y = y + set2;
    }

    // Add stored values
    int z = x + y;

    // Determine if total is a multiple of 10
    z = z % 10;

    // If it is, checksum is passed
    if (z == 0)
    {

        // Assign original long n to num
        long num = n1;

        // Loop through long n
        while (num >= 100)
        {

            // Cut digits off end of long n until remainder is in range for checks
            num = num / 10;
        }

        // Identifies American Express cards
        if (strlen(str) == 15 && (num == 34 || num == 37))
        {
            printf("AMEX\n");
        }

        // Identifies Mastercards
        else if (strlen(str) == 16 && (num >= 51 && num <= 55))
        {
            printf("MASTERCARD\n");
        }

        // Identifies Visa cards
        else if ((strlen(str) == 13 || strlen(str) == 16) && (num >= 40 && num <= 49))
        {
            printf("VISA\n");
        }

        // If none of the above
        else
        {
            printf("INVALID\n");
        }
    }

    // Otherwise checksum has failed
    else
    {
        printf("INVALID\n");
    }
}

// Function ensures user input is correct length
long get_number(void)
{

    // Variable to use within function
    long card_length;
    do
    {

        // Asks user for input
        card_length = get_long("Number: ");
    }

    // Defines range
    while ((card_length >= 13 && card_length <= 16) && (card_length != 14));

    // If within range, returns original number
    return card_length;
}