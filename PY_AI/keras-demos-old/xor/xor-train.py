#!/usr/bin/env python

import numpy as np
from keras.models import Sequential
from keras.layers.core import Activation, Dense

training_data = np.array([[0,0],[0,1],[1,0],[1,1]], "float32")
target_data = np.array([[0],[1],[1],[0]],"float32")

#Create the model
model = Sequential()

#Input Layer -> Regular activation (with input dimension -> 2)
model.add(Dense(32, input_dim=2, activation='relu'))
#Output layer -> 1 output node in the layer with sigmoid
model.add(Dense(1, activation='sigmoid'))

#Setup the loss, optimizer and metrics functions
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['binary_accuracy'])

#Perform training
model.fit(training_data, target_data, epochs=1000, verbose=2)

#Run the network with test input
print('Running base training data model...')
print(model.predict(training_data))

#Store trained model
model.save("xor")

input('Persisted trained model...')

#Testing output
input('Running test on given input...')
test = [[1, 0]]
print('The network output was: ' + str(int(round(model.predict(test)[0][0]))))

input('Press any key to exit...')