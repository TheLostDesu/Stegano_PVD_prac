from PIL import Image
from math import log2, ceil
from numpy import array, uint8

def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

def frombits(bits):
    chars = []
    for b in range(len(bits) // 8):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

def toint(b):
    ans = 0
    for i in b:
        ans *= 2
        ans += i
    return ans

def tobits2(i):
    bits = []
    while i:
        bits.append(i % 2)
        i //= 2
    return bits[::-1]


intervals = [0, 8, 16, 32, 64, 128, 256]


img = Image.open('out.png')
pixels = list(img.getdata())
msg = []


for i in range(0, len(pixels), 2):
    Pi = pixels[i][1]
    Pk = pixels[i + 1][1]

    dk = abs(Pk - Pi)
    uk = list(filter(lambda i: i > abs(dk), intervals))[0]
    lk = intervals[intervals.index(uk) - 1]
    uk -= 1
    nk = int(log2(uk - lk + 1))

    mk = dk - lk
    mk = tobits2(mk)
    for j in range(nk - len(mk)):
        msg.append(0)
    for j in mk:
        msg.append(j)

    if len(msg) > 15 and 0 not in msg[-15:]:
        break

print(frombits(msg))