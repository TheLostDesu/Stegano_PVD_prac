from PIL import Image
from math import log2, ceil, floor
from numpy import array, uint8

def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result


def toint(b):
    ans = 0
    for i in b:
        ans *= 2
        ans += i
    return ans


intervals = [0, 8, 16, 32, 64, 128, 256]

def to_encode(text):
    msg = tobits(text)
    for i in range(20):
        msg.append(1)
    iter_in_msg = 0



    img = Image.open('in.jpg')
    pixels = list(img.getdata())
    width, height = img.size


    for i in range(0, len(pixels), 2):
        Pi = pixels[i][1]
        Pk = pixels[i + 1][1]

        dk = Pk - Pi
        uk = list(filter(lambda i: i > abs(dk), intervals))[0]
        lk = intervals[intervals.index(uk) - 1]
        uk -= 1
        nk = int(log2(uk - lk + 1))
        mk = []

        for k in range(nk):
            if iter_in_msg < len(msg):
                mk.append(msg[iter_in_msg])
                iter_in_msg += 1
        mk = toint(mk)

        if dk >= 0:
            dkn = lk + mk
        else:
            dkn = -(lk + mk)


        if dk % 2 != 0:
            Pni = Pi - ceil((dkn - dk) / 2)
            Pnk = Pk + floor((dkn - dk) / 2)
        else:
            Pni = Pi - floor((dkn - dk) / 2)
            Pnk = Pk + ceil((dkn - dk) / 2)
            

        pixels[i] = (pixels[i][0], Pni, pixels[i][2])
        pixels[i + 1] = (pixels[i + 1][0], Pnk, pixels[i + 1][2])

        if iter_in_msg >= len(msg):
            break


    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    new_image = Image.fromarray(array(pixels, dtype=uint8))
    new_image.save('out.png')

