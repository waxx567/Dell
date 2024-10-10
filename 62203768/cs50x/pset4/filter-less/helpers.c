#include "helpers.h"
#include <math.h>

// Declare colours for blur function
#define RED_COLOR 0
#define GREEN_COLOR 1
#define BLUE_COLOR 2

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop through rows
    for (int row = 0; row < height; row++)
    {
        // Loop through columns
        for (int col = 0; col < width; col++)
        {
            // Store the average value of the 3 colours in the rgbtGray variable, rounding the floating point result
            int rgbtGray = round(((image[row][col].rgbtRed) + (image[row][col].rgbtGreen) + (image[row][col].rgbtBlue)) / 3.0);

            // Assign that value to each of the colours
            image[row][col].rgbtRed = rgbtGray;
            image[row][col].rgbtGreen = rgbtGray;
            image[row][col].rgbtBlue = rgbtGray;
        }
    }
    // Exit function
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop through rows
    for (int row = 0; row < height; row++)
    {
        // Loop through columns
        for (int col = 0; col < width; col++)
        {
            // Transform pixels to sepia values, rounding the floating point results
            int sepiaRed =
                round(.393 * image[row][col].rgbtRed + .769 * image[row][col].rgbtGreen + .189 * image[row][col].rgbtBlue);
            int sepiaGreen =
                round(.349 * image[row][col].rgbtRed + .686 * image[row][col].rgbtGreen + .168 * image[row][col].rgbtBlue);
            int sepiaBlue =
                round(.272 * image[row][col].rgbtRed + .534 * image[row][col].rgbtGreen + .131 * image[row][col].rgbtBlue);

            // Set to 255 if any of the new values is above 255
            image[row][col].rgbtRed = fmin(255, sepiaRed);
            image[row][col].rgbtGreen = fmin(255, sepiaGreen);
            image[row][col].rgbtBlue = fmin(255, sepiaBlue);
        }
    }
    // Exit function
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Temporary variable to store pixel values
    RGBTRIPLE temp;

    // Loop through rows
    for (int row = 0; row < height; row++)
    {
        // Loop through half of the columns otherwise the loop will return all to their original values
        for (int col = 0; col < width / 2; col++)
        {
            // Set current pixel values as temp variable values
            temp = image[row][col];
            // Set current pixel values to values of reflected pixel
            image[row][col] = image[row][width - col - 1];
            // Set reflected pixel values to current pixel values
            image[row][width - col - 1] = temp;
        }
    }
    // Exit function
    return;
}

// Function to be called by the blur function below it
// Function calculates the average of the values of the surrounding pixels and returns that value as an integer
int boxBlur(int i, int j, int height, int width, RGBTRIPLE image[height][width], int color_base)
{
    // Start a counter
    float counter = 0;
    // Start a running total
    int total = 0;

    // Inspect the pixels to the left and right
    for (int row = (i - 1); row <= (i + 1); row++)
    {
        // Inspect the pixels at the top and below
        for (int col = (j - 1); col <= (j + 1); col++)
        {
            // If out of this range, leave loop
            if (row < 0 || row >= height || col < 0 || col >= width)
            {
                continue;
            }

            // Add to the total by colour
            if (color_base == RED_COLOR)
            {
                total += image[row][col].rgbtRed;
            }
            else if (color_base == GREEN_COLOR)
            {
                total += image[row][col].rgbtGreen;
            }
            else
            {
                total += image[row][col].rgbtBlue;
            }
            // Increment counter
            counter++;
        }
    }
    // Return average, rounding the floating point number to be expressed as an integer
    return round(total / counter);
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Temporary variable to store pixel values
    RGBTRIPLE temp[height][width];

    // Loop through rows
    for (int row = 0; row < height; row++)
    {
        // Loop through columns
        for (int col = 0; col < width; col++)
        {
            // Set temp values to mirror current values
            temp[row][col] = image[row][col];
        }
    }

    // Loop through rows
    for (int row = 0; row < height; row++)
    {
        // Loop through columns
        for (int col = 0; col < width; col++)
        {
            // Reset current values by calling boxBlur function
            image[row][col].rgbtRed = boxBlur(row, col, height, width, temp, RED_COLOR);
            image[row][col].rgbtGreen = boxBlur(row, col, height, width, temp, GREEN_COLOR);
            image[row][col].rgbtBlue = boxBlur(row, col, height, width, temp, BLUE_COLOR);
        }
    }
    // Exit function
    return;
}