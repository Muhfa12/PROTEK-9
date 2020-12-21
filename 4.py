#4
import random
def shuffleString(x, n):
    hasil = []
    a = list(x)
    for i in range(n):
        b = "".join(random.sample(a, len(a)))
        c = b in hasil
        if c == False:
            hasil = hasil + [b]
    return hasil
print(shuffleString("aku", 2))
print(shuffleString("aku", 3))
print(shuffleString("aku", 3))

