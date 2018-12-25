import math
import random
def squarrt(x):
    assert x >= 0
    y = math.sqrt(x)
    assert y * y == x
    return y

for i in range(1,1000):
    r = random.random() * 10000
    try:
        z = squarrt(r)
    except:
        print r, math.sqrt(r) * math.sqrt(r)
        break
print "done!"
