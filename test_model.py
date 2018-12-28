import keras
import numpy as np

file_name = input("Model File:")
input_length = int(input("input_length"))
dummy_input = [ord(dum) for dum in input("Dummy Input?")]

input_sequence = [dummy_input[i%len(dummy_input)] for i in range(input_length)]
model = keras.models.load_model(file_name)
out = ''
for _ in range(int(input("Characters to generate"))):

    try:
        prediction = np.array([[[int(i == el) for i in range(256)] for el in input_sequence]])
        # print(prediction)
        input_sequence+=[model.predict_classes(prediction, verbose = 0)]
        # print("SUCCEDED GOT:",end = '')
        out+=chr(input_sequence[-1])
        input_sequence = input_sequence[1:]
    except:
        print("FAILED ON!")
        print(prediction)

print(dummy_input)
print("---predicted rest---")
print(out)


