/*
Implement a program called recover that recovers JPEGs from a forensic image.

Implement your program in a file called recover.c in a directory called recover.
Your program should accept exactly one command-line argument, the name of a forensic image from which to recover JPEGs.
If your program is not executed with exactly one command-line argument, it should remind the user of correct usage, and main should
return 1. If the forensic image cannot be opened for reading, your program should inform the user as much, and main should return 1.
The files you generate should each be named ###.jpg, where ### is a three-digit decimal number, starting with 000 for the first
image and counting up. Your program, if it uses malloc, must not leak any memory.
*/

#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef uint8_t BYTE;        // Declare byte type
#define BLOCK_SIZE 512       // Define block size in bytes
bool jpgGood(BYTE buffer[]); // Declare function for validating JPEGs

int main(int argc, char *argv[])
{
    // If user does not provide two arguments only - exit program with message and error code 1
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    // Open forensic file - if file cannot be opened, exit program with message and error code 1
    FILE *forensicFile = fopen(argv[1], "r");
    if (forensicFile == NULL)
    {
        printf("%s could not be opened.\n", argv[1]);
        return 1;
    }

    bool found = false;      // Store JPEG status
    BYTE buffer[BLOCK_SIZE]; // Buffer to store blocks
    char filename[8];        // Store file name
    int count = 0;           // JPEG counter
    FILE *outFile = NULL;    // Pointer to write file

    // Read 512 bytes from memory card into buffer - do not read end of file character
    while (fread(buffer, sizeof(BYTE), BLOCK_SIZE, forensicFile) || feof(forensicFile) == 0)
    {
        // If this is a JPEG
        if (jpgGood(buffer))
        {
            // Close previous JPEG if it is still open
            if (found && count != 0)
            {
                fclose(outFile);
            }

            // No JPEG was open, mark this one as found
            else
            {
                found = true;
            }

            sprintf(filename, "%03i.jpg", count); // Generate numbered file name
            count++;                              // Update counter
            outFile = fopen(filename, "w");       // Open file to write to

            // Write to file if outFile opens without an issue
            if (outFile != NULL)
            {
                fwrite(buffer, sizeof(buffer), 1, outFile);
            }

            // If file cannot be opened, exit program with message and error code 1
            else
            {
                printf("%s could not be opened.\n", filename);
                return 1;
            }
        }
    }

    fclose(forensicFile); // Close input file
    found = false;        // Reset JPEG status

    // Close outFile if still open
    if (found)
    {
        fclose(outFile);
    }

    // Exit program with success code 0
    return 0;
}

// Function to check if first four bytes indicate file is a JPEG
bool jpgGood(BYTE buffer[])
{
    return buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0;
}