import random
from string import ascii_lowercase
from encrypt import to_encode
from value import test_inv

def generate_random_string(length):
    letters = ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


for i in range(1000, 10000, 1000):
    txt = generate_random_string(i)
    to_encode(txt)
    
    print(len(txt), *test_inv())

    

