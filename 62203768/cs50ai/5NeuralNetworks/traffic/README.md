# Notes on CS50Ai Project 5: Traffic

[Link](https://cs50.harvard.edu/ai/2024/projects/5/traffic/)

Write an AI to identify which traffic sign appears in a photograph.

**Example**

    $ python traffic.py gtsrb
    Epoch 1/10
    500/500 [==============================] - 5s 9ms/step - loss: 3.7139 - accuracy: 0.1545
    Epoch 2/10
    500/500 [==============================] - 6s 11ms/step - loss: 2.0086 - accuracy: 0.4082
    Epoch 3/10
    500/500 [==============================] - 6s 12ms/step - loss: 1.3055 - accuracy: 0.5917
    Epoch 4/10
    500/500 [==============================] - 5s 11ms/step - loss: 0.9181 - accuracy: 0.7171
    Epoch 5/10
    500/500 [==============================] - 7s 13ms/step - loss: 0.6560 - accuracy: 0.7974
    Epoch 6/10
    500/500 [==============================] - 9s 18ms/step - loss: 0.5078 - accuracy: 0.8470
    Epoch 7/10
    500/500 [==============================] - 9s 18ms/step - loss: 0.4216 - accuracy: 0.8754
    Epoch 8/10
    500/500 [==============================] - 10s 20ms/step - loss: 0.3526 - accuracy: 0.8946
    Epoch 9/10
    500/500 [==============================] - 10s 21ms/step - loss: 0.3016 - accuracy: 0.9086
    Epoch 10/10
    500/500 [==============================] - 10s 20ms/step - loss: 0.2497 - accuracy: 0.9256
    333/333 - 5s - loss: 0.1616 - accuracy: 0.9535

## Background

As research continues in the development of self-driving cars, one of the key challenges is computer vision, allowing these cars to develop an understanding of their environment from digital images. In particular, this involves the ability to recognize and distinguish road signs – stop signs, speed limit signs, yield signs, and more.

In this project, you’ll use TensorFlow to build a neural network to classify road signs based on an image of those signs. To do so, you’ll need a labeled dataset: a collection of images that have already been categorized by the road sign represented in them.

Several such data sets exist, but for this project, we’ll use the German Traffic Sign Recognition Benchmark (GTSRB) dataset, which contains thousands of images of 43 different kinds of road signs.

