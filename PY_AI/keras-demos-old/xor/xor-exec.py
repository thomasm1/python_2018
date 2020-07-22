import numpy as np
from keras.models import load_model

print('Loading trained XOR model...')
model = load_model('xor')

print('Model successfully loaded')

def run_network(input_data):
    print('Network Output /w '+ str(input_data[0]) + ' -> ' + str(int(round(model.predict(input_data)[0][0]))))

#Predict with user input
run_network([[0,0]])
run_network([[0,1]])
run_network([[1,0]])
run_network([[1,1]])