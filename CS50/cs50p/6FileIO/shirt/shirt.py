from os.path import splitext
from PIL import Image, ImageOps
import sys


def main():

    check_args()
    # Try to open image
    try:
        image = Image.open(sys.argv[1])
    # If image not found
    except FileNotFoundError:
        sys.exit("Input does not exist")
    # Open shirt
    shirt = Image.open("shirt.png")
    # Get shirt size
    size = shirt.size
    # Fit image to shirt size
    resizeImage = ImageOps.fit(image, size)
    # Paste resized image on shirt
    resizeImage.paste(shirt, shirt)
    # Save to output file
    resizeImage.save(sys.argv[2])


''' Function to check command-line arguments '''
def check_args():

    # Ensure correct number of command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Ensure file extensions are valid
    inFile = splitext(sys.argv[1])
    outFile = splitext(sys.argv[2])

    fileTypes = [".jpg", ".jpeg", ".png"]

    if inFile[1] not in fileTypes:
        sys.exit("Invalid input")
    if outFile[1] not in fileTypes:
        sys.exit("Invalid output")

    # Ensure file extensions are the same
    if inFile[1].lower() != outFile[1].lower():
        sys.exit("Input and output have different extensions")


if __name__ =="__main__":
    main()