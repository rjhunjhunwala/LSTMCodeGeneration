out = ""
for i in range(5):
    for j in range(26):
        out += chr(65+j)
for i in range(10):
    for j in range(10):
        out += str(j)
for i in range(5):
    for j in range(26):
        out += chr(65+j)
with open("noise.txt","w") as fil:
    fil.write(out)