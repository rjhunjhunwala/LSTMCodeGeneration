import numpy as np
from pickle import dump
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
INPUT_SEQUENCE_LENGTH = 100
VOCAB_SIZE = 256

X = []
y = []
s = ""
with open("code.txt","r") as fil:
    s = fil.read()
for i in range(0, 8000):#len(s)-INPUT_SEQUENCE_LENGTH-1):
    X.append([ord(a) for a in s[i:i+INPUT_SEQUENCE_LENGTH]])
    y.append(ord(s[i+INPUT_SEQUENCE_LENGTH]))

X = [[[int(i == el) for i in range(VOCAB_SIZE)]for el in seq] for seq in X]
y = [[int(i == el) for i in range(VOCAB_SIZE)] for el in y]

X = np.array(X)
y = np.array(y)
model = Sequential()
model.add(LSTM(70, return_sequences = True, input_shape = (INPUT_SEQUENCE_LENGTH, VOCAB_SIZE)))
model.add(LSTM(70))
model.add(Dense(VOCAB_SIZE, activation='softmax'))
print(model.summary())
model.compile(loss='categorical_crossentropy',optimizer='adam')
model.fit(X ,y,epochs = 100, verbose = 2)
model.save("alphabetmodel.h5")