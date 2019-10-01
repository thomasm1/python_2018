# https://www.tensorflow.org/tutorials/keras/classification#train_the_model
# ENV: pipenv
# installs:  tensorflow==2.0.0-rc1 matplotlib pandas

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

data = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = data.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images = train_images/255.0  # optional, shrink data- easier to work with
test_images = test_images/255.0  # optional, shrink data- easier to work with

# print(train_images[7]) # show data & image
# print(train_labels[6]) # show image
# plt.imshow(train_images[7], cmap=plt.cm.binary)
# plt.show()

# Input Layer:   (28 x 28)
# [[0,0.1,0.3...]
#  [0 .....    ]]  must flatten data to list of length 784 for input layer to neural network;
# Output Layer:  0 - 9
# 0: 0.05 When training: => 0 ... network adjusts weights accordingly
# 1: 0.10 When training: => 0... network adjusts weights accordingly
# ....
# 6: 0.75   When training: => 1... network adjusts weights accordingly

# Weights and Biases: 784 x 10 ...
# Then add intermediary, hidden layer of any (128) (inputs to hid layer, hid layer to outputs) to find patterns
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)), # flatten inputs to list-array
    keras.layers.Dense(128, activation="relu"),  # rectified linear unit - hidden layer
    keras.layers.Dense(10, activation="softmax") # output - 10 functions
])
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
model.fit(train_images, train_labels, epochs=5)

test_loss, test_acc = model.evaluate(test_images, test_labels) # loss: .2822;  accuracy: .8719
print("tested Acc: ", test_acc)