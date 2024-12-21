#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "wav.h"

int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{
    /* .wav files have 3 chunks
        The first chunk contains information about the file’s type. In particular, see how the “File Format” block in the first
       chunk spells out ‘W’ ‘A’ ‘V’ ‘E’ in bytes 8–11, to indicate the file is a WAV file. The second chunk contains information
       about the upcoming audio data, including how many “channels” of audio are present and how many bits are in each audio
       “sample”. Audio files have 1 channel when they’re “monophonic”: if you were to wear headphones, you’d hear the same audio in
       your left and right ear. Audio files have 2 channels when they’re “stereophonic”: wearing headphones, you’d hear slightly
       different audio in your left and right ear, creating a sense of spaciousness. Samples are the individual chunks of bits which
       make up the audio you hear. With more bits per sample, an audio file can have greater clarity (at the cost of more memory
       used!). Finally, the third chunk contains the audio data itself—those samples we mentioned just above. Everything before the
       audio data is considered part of the WAV “header”. Recall that a file header is simply some metadata about the file. In this
       case, the header is 44 bytes long.
    */

    // Ensure proper usage // TODO #1
    // Print message if user does not provide three arguments only and exit with error code 1
    if (argc != 3)
    {
        printf("Usage: ./reverse input.wav output.wav\n");
        return 1;
    }

    // Open input file for reading // TODO #2
    char *infile = argv[1];            // Store user input
    FILE *inptr = fopen(infile, "rb"); // Open input file as inptr

    // Print message if file could not be opened and exit with error code 1
    if (inptr == NULL)
    {
        printf("%s could not be opened.", infile);
        return 1;
    }

    // Read header // TODO #3
    WAVHEADER header;                            // Declare struct to analyse header
    fread(&header, sizeof(WAVHEADER), 1, inptr); // Read input file into struct

    // Use check_format to ensure WAV format // TODO #4
    // If input file is a WAV file
    if (check_format(header) == 0)
    {
        // Open output file for writing // TODO #5
        char *outfile = argv[2];             // Store user input
        FILE *outptr = fopen(outfile, "wb"); // Open output file as outptr

        // Print message if file could not be opened and exit with error code 1
        if (outptr == NULL)
        {
            printf("%s could not be opened.", outfile);
            return 1;
        }

        // Write header to file // TODO #6
        fwrite(&header, sizeof(WAVHEADER), 1, outptr); // Write header data to output file

        // Use get_block_size to calculate size of block // TODO #7
        int size = get_block_size(header);

        // Write reversed audio to file // TODO #8
        // Print message if there is a file already open and exit with error code 1
        if (fseek(inptr, size, SEEK_END))
        {
            printf("Write failed.\n");
            return 1;
        }

        BYTE buffer[size]; // Store data chunk

        // Loop until file pointer's position is header size minus the size of the current block
        while (ftell(inptr) - size > sizeof(header))
        {
            // Print message if there is a file already open and exit with error code 1
            if (fseek(inptr, -2 * size, SEEK_CUR))
            {
                printf("Write failed.\n");
                return 1;
            }
            fread(buffer, size, 1, inptr);
            // read backwards

            fwrite(buffer, size, 1, outptr);
        }

        fclose(outptr); // Close output file
        fclose(inptr);  // Close input file
    }
}

int check_format(WAVHEADER header)
{
    // Use check_format to ensure WAV format // TODO #4
    if (header.format[0] == 'W' && header.format[1] == 'A' && header.format[2] == 'V' && header.format[3] == 'E')
    {
        if (header.audioFormat != 1)
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }
    else
    {
        printf("Input is not a WAV file.\n");
        return 1;
    }
}

int get_block_size(WAVHEADER header)
{
    // TODO #7
    int blocksize = header.numChannels * header.bitsPerSample / 8;
    return blocksize;
}