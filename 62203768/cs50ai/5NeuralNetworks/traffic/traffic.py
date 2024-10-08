import os
import sys
import cv2
import numpy as np
import tensorflow as tf

from sklearn.model_selection import train_test_split

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # Get image arrays and labels for all image files
    images, labels = load_data(sys.argv[1])

    # Split data into training and testing sets
    labels = tf.keras.utils.to_categorical(labels)
    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=TEST_SIZE
    )

    # Get a compiled neural network
    model = get_model()

    # Fit model on training data
    model.fit(x_train, y_train, epochs=EPOCHS)

    # Evaluate neural network performance
    model.evaluate(x_test,  y_test, verbose=2)

    # Save model to file
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        model.save(filename)
        print(f"Model saved to {filename}.")


# The `load_data` function should accept as an argument `data_dir`, representing the path to a directory where the data is stored, and return image arrays and labels for each image in the data set.
def load_data(data_dir):
    """
    Load image data from directory `data_dir`.

    Assume `data_dir` has one directory named after each category, numbered
    0 through NUM_CATEGORIES - 1. Inside each category directory will be some
    number of image files.

    Return tuple `(images, labels)`. `images` should be a list of all
    of the images in the data directory, where each image is formatted as a
    numpy ndarray with dimensions IMG_WIDTH x IMG_HEIGHT x 3. `labels` should
    be a list of integer labels, representing the categories for each of the
    corresponding `images`.
    """
    # Create empty lists to hold values
    images = []
    labels = []

    # Iterate over the folders in the directory
    for folder in os.listdir(data_dir):
        # Error check: ensure the folder exists
        try:
            int(folder)
        except ValueError:
            print(f"Error: {int(folder)} folder not found")
            continue

        # Iterate over the files (images) in the folder
        for file in os.listdir(os.path.join(data_dir, folder)):
            # Open and resize the image
            image = cv2.imread(os.path.join(data_dir, folder, file))
            img = cv2.resize(image, (IMG_WIDTH, IMG_HEIGHT))
            # Normalize the image
            img = img / 255
            # Append the image to the images list and the folder name to the labels list
            images.append(img)
            labels.append(folder)

    # Error check: number of images must match number of labels
    if len(images) != len(labels):
        sys.exit(f"Error: number of images ({len(images)
                                             }) did not match number of labels ({len(labels)})")

    return (images, labels)


# The `get_model` function should return a compiled neural network model.
def get_model():
    """
    Returns a compiled convolutional neural network model. Assume that the
    `input_shape` of the first layer is `(IMG_WIDTH, IMG_HEIGHT, 3)`.
    The output layer should have `NUM_CATEGORIES` units, one for each category.
    """

    # Create a convolutional neural network
    model = tf.keras.models.Sequential([

        # Convolutional layer x 2
        # Learn 64 filters using a 3x3 kernel
        tf.keras.layers.Conv2D(
            64, (3, 3), activation="relu", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
        ),
        # Max-pooling layer, using 2x2 pool size
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        # Learn 64 filters using a 3x3 kernel
        tf.keras.layers.Conv2D(
            64, (3, 3), activation="relu",
        ),
        # Max-pooling layer, using 2x2 pool size
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

        # Flatten units
        tf.keras.layers.Flatten(),

        # Add a hidden layer with dropout
        tf.keras.layers.Dense(512, activation="relu"),
        tf.keras.layers.Dropout(0.5),

        # Add an output layer with output units for however many categories are stored in the NUM_CATEGORIES variable
        tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax")
    ])

    # Compile neural network
    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )

    return model


if __name__ == "__main__":
    main()
