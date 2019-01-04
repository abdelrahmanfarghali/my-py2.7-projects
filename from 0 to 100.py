import random
d = []
for e in range(1,101):
    d.append(e)
z = d
s = random.randint(1,100)
d.pop(d.index(s))

k = 0
for e in range(1,len(d)):
    try:
        d.index(e)
        pass
    except (ValueError):
        print e
