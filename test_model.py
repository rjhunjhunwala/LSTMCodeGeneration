import keras
import numpy as np

file_name = input("Model File:")
input_length = int(input("input_length"))
dummy_input = [ord(dum) for dum in input("Dummy Input?")]

input_sequence = [dummy_input[i%len(dummy_input)] for i in range(input_length)]
model = keras.models.load_model(file_name)

for _ in range(int(input("Characters to generate"))):

    prediction = np.array([[[i == el for i in range(256)] for el in input_sequence]])
    input_sequence+=[model.predict_classes(prediction, verbose = 0)]
    print(chr(input_sequence[-1]),end = '')
    input_sequence = input_sequence[1:]






