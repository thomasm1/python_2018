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

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)), # flatten 
    keras.layers.Dense(128, activation="relu"),  # rectified linear unit - hidden layer
    keras.layers.Dense(10, activation="softmax") # output - 10 functions
])
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
model.fit(train_images, train_labels, epochs=5)

# test_loss, test_acc = model.evaluate(test_images, test_labels) # loss: .2822;  accuracy: .8719
# print("tested Acc: ", test_acc)

prediction = model.predict(test_images)    # [7])

for i in range(5):
    plt.grid(False)
    plt.imshow(test_images[i], cmap.plt.cm.binary)
    plt.xlabel("Actual: " + class_names[test_labels[i]])
    plt.title("Prediction: " + class_names[np.argmax(prediction[i])])
    plt.show()