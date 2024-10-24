// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

// Define type to store unsigned integers that are 8 bits (1 byte) each
typedef uint8_t BYTE;
// Define type to store signed integers that are 16 bits (2 bytes) each
typedef int16_t SAMPLE;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);

    // Buffer to store header bytes
    BYTE header_buffer[HEADER_SIZE];

    // TODO: Copy header from input file to output file
    fread(header_buffer, sizeof(BYTE), HEADER_SIZE, input);
    fwrite(header_buffer, sizeof(BYTE), HEADER_SIZE, output);

    // TODO: Read samples from input file and write updated data to output file
    // Buffer to store 2 byte samples
    SAMPLE buffer;

    // Loop through input file to end and read each sample into memory
    // Update volume and write updated sample to output file
    while (fread(&buffer, sizeof(SAMPLE), 1, input) == 1)
    {
        buffer = buffer * factor;
        fwrite(&buffer, sizeof(SAMPLE), 1, output);
    }

    // Close files
    fclose(input);
    fclose(output);
}