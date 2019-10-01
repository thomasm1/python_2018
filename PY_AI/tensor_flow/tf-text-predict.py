import tensorflow as tf
from tensorflow import keras
import numpy as np

data = keras.datasets.imdb

(train_data, train_labels), (test_data, test_labels) = data.load_data(num_words=88000)
# print(train_data[0])
 
word_index = data.get_word_index()

word_index = {k:(v+3) for k, v in word_index.items()}
word_index["<PAD>"] = 0
word_index["<START>"] = 1
word_index["<UNK>"] = 2
word_index["<UNUSED>"] = 3 

reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

train_data = keras.preprocessing.sequence.pad_sequences(train_data, value=word_index["<PAD>"], padding="post", maxlen=250)
test_data = keras.preprocessing.sequence.pad_sequences(test_data, value=word_index["<PAD>"], padding="post", maxlen=250)

# print(len(train_data), len(test_data))

def decode_review(text):
    return " ".join([reverse_word_index.get(i, "?") for i in text])
# print(decode_review(test_data[0]))

# print(len(test_data[0]), len(test_data[1]))
model = keras.Sequential()
model.add(keras.layers.Embedding(88000, 16))  # 1.) limit 88000 word-vectors; 2.) 16 vectors per-word embedding context
model.add(keras.layers.GlobalAveragePooling1D()) # 3.) consolidate embedding
model.add(keras.layers.Dense(16, activation="relu")) # 4.) rect. linear unit - functions
model.add(keras.layers.Dense(1, activation="sigmoid")) # 5.) outputs in range (0, 1), ideal for binary class"n to find probability of data belonging to class.
model.summary()
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"]) # 6.) (Unlike Softmax loss) Independent for each vector component (class)

x_val = train_data[:10000] # x-validation
x_train = train_data[10000:]

y_val = train_labels[:10000]
y_train = train_labels[10000:]

fitModel = model.fit(x_train, y_train, epochs=40, batch_size=512, validation_data=(x_val, y_val), verbose=1) # 512 reviews/40 versions; 
#fitModel = model.fit(x_train, y_train, epochs=10, batch_size=512, validation_data=(x_val, y_val), verbose=1) # 512 reviews/10 versions; 

results = model.evaluate(test_data, test_labels)
print(results)  # loss .3298  accuracy: 0.8716

test_review = test_data[0]
predict = model.predict([test_review])
print("Review: ")
print(decode_review(test_review))
print("Actual: " + str(test_labels[0]))  # 0 

# print("Prediction: " + str(predict[0]))  # 0 bad review ... correct!!  [using 40 epochs]
# print(results)    # loss .33136 accuracy: 0.87112 [using 40 epochs]
print("Prediction: " + str(predict[0]))  # 0.002196 bad review ... less sure, but correct  [using 10 epochs]
print(results)    # loss .3958 accuracy: 0.8492 [using 10 epochs] ... 0.02192 less accurate using 30 less epochs... 

model.save("model.h5")