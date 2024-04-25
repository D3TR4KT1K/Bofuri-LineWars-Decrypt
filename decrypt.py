from itertools import cycle
import os

def xor(data: bytes, key: bytes) -> bytes:
    return bytes(i^j for i,j in zip(data, cycle(key)))

key = b"gzjZZiWUynuw57jri6LMrN8ujQwakGMTECFwybJw5Tk7LZ35Wd27Cm2jJrwpcAXM"

filelist = os.listdir()

for x in filelist:
    if not x.endswith(".py"):
        file = open(x, "rb").read()
        open(x + "_dec", "wb").write(xor(file, key))
        print("Decrypted: ", x)