/*
Implement a program called recover that recovers JPEGs from a forensic image.

Implement your program in a file called recover.c in a directory called recover.
Your program should accept exactly one command-line argument, the name of a forensic image from which to recover JPEGs.
If your program is not executed with exactly one command-line argument, it should remind the user of correct usage, and main should return 1.
If the forensic image cannot be opened for reading, your program should inform the user as much, and main should return 1.
The files you generate should each be named ###.jpg, where ### is a three-digit decimal number, starting with 000 for the first image and counting up.
Your program, if it uses malloc, must not leak any memory.
*/

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

// Declare byte type
typedef uint8_t BYTE;

// Define block size in bytes
#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{
    // If user does not provide two arguments only, exit program with message and error code 1
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    // Store user input in a variable
    char *file = argv[1];

    // Open forensic file. If file cannot be opened, exit program with message and error code 1
    FILE *raw_file = fopen(argv[1], "r");
    if (raw_file == NULL)
    {
        printf("%s could not be opened.", file);
        return 1;
    }

    // Buffer to store blocks
    BYTE buffer[BLOCK_SIZE];
    // Store file name
    char file_name[8];
    // JPEG counter
    int count = 0;
    // Pointer to current file
    FILE *pointer = NULL;

    while (fread(buffer, BLOCK_SIZE, 1, raw_file))
    {
        // If this is a JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // If this is not the first JPEG, close the previous JPEG
            // Generate numbered file name, open file and write to file
            if (count > 0)
            {
                fclose(pointer);
                sprintf(file_name, "%03d.jpg", count);
                pointer = fopen(file_name, "w");
                fwrite(buffer, BLOCK_SIZE, 1, pointer);
            }
            // If this is the first JPEG
            // Generate numbered file name, open file and write to file
            else if (count == 0)
            {
                sprintf(file_name, "%03d.jpg", count);
                pointer = fopen(file_name, "w");
                fwrite(buffer, BLOCK_SIZE, 1, pointer);
            }
            // Increment count for next file name number
            count++;
        }
    }


    // Open memory card
    // Look for JPEG
    // Open JPEG
    // Write 512 bytes until new JPEG found
}