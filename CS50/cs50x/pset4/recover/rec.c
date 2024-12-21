/*
Implement a program called recover that recovers JPEGs from a forensic image.

Implement your program in a file called recover.c in a directory called recover.
Your program should accept exactly one command-line argument, the name of a forensic image from which to recover JPEGs.
If your program is not executed with exactly one command-line argument, it should remind the user of correct usage, and main should return 1.
If the forensic image cannot be opened for reading, your program should inform the user as much, and main should return 1.
The files you generate should each be named ###.jpg, where ### is a three-digit decimal number, starting with 000 for the first image and counting up.
Your program, if it uses malloc, must not leak any memory.
*/

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

// Declares byte type
typedef uint8_t BYTE;

// Define block size in bytes
#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{
    // If user does not input two arguments only, exits program with message and error code 1
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    // Stores user input
    char *file = argv[1];

    // Opens forensic file
    FILE *raw_file = fopen(argv[1], "r");
    // If file could not be opened, exits program with message and error code 1
    if (raw_file == NULL)
    {
        printf("%s could not be opened.", file);
        return 1;
    }

    // Stores whether JPEG found or not
    bool found = false;
    // Counts JPEGs found
    int count = 0;
    // Buffer to store block
    BYTE buffer[BLOCK_SIZE];
    // Stores file name
    char current_name[10];
    // Pointer to current file
    FILE *pointer = NULL;

    // Reads forensic file block by block
    while (fread(buffer, BLOCK_SIZE, 1, raw_file) == 1)
    {

        // If this is a JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // Closes previous JPEG if it is still open
            if (found && count != 0)
            {
                fclose(pointer);
            }
            // Otherwise JPEG has been found
            else
            {
                found = true;
            }
        }

        // Generates numbered file name
        sprintf(current_name, "%03d.jpg", count);

        // Opens file with that name
        pointer = fopen(current_name, "w");
        // If file could not be created, exits program with message and error code 1
        if (pointer == NULL)
        {
            fclose(raw_file);
            printf("%s could not be created.", current_name);
            return 1;
        }
        // Increments JPEG count by one
        count++;
    }

    // If JPEG open, writes block to file
    if (found)
    {
        fwrite(buffer, BLOCK_SIZE, 1, pointer);
    }

    // Closes forensic file
    fclose(raw_file);
    // If JPEG file open, closes it
    if (found)
    {
        fclose(pointer);
    }

    // Exits program with success code 0
    return 0;
}