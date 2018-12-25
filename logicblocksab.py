a = raw_input("A")
b = raw_input("B")
s = raw_input(":")
s0 = s[0]
s1 = s[1]
s2 = s[2]
s3 = s[3]
def andiii(a,b,c):
    if a == 0 and b == 0 and c == 0:
        return 0
    if a == 1 and b == 0 and c == 0:
        return 0
    if a == 0 and b == 1 and c == 0:
        return 0
    if a == 1 and b == 1 and c == 0:
        return 0
    if a == 0 and b == 1 and c == 1:
        return 0
    if a == 1 and b == 0 and c == 1:
        return 0
    if a == 1 and b == 1 and c == 1:
        return 1
def orii(a,b):
    if a == 0 and b == 0:
        return 0
    if a == 0 and b == 1:
        return 1
    if a == 1 and b == 0:
        return 1
    if a == 1 and b == 1:
        return 1
def andii(a,b):
    if a == 0 and b == 0:
        return 0
    if a == 0 and b == 1:
        return 0
    if a == 1 and b == 0:
        return 0
    if a == 1 and b == 1:
        return 1
def oriii(a,b,c):
    if a == 0 and b == 0 and c == 0:
        return 0
    if a == 1 and b == 0 and c == 0:
        return 1
    if a == 0 and b == 1 and c == 0:
        return 1
    if a == 1 and b == 1 and c == 0:
        return 1
    if a == 0 and b == 1 and c == 1:
        return 1
    if a == 1 and b == 0 and c == 1:
        return 1
    if a == 1 and b == 1 and c == 1:
        return 1
def noti(x):
    if x == 1:
        return 0
    else:
        return 1

g01 = andiii(b,s3,a)
g02 = andiii(a,s2,noti(b))
g = orii(g01,g02)
p01 = andii(noti(b),s1)
p02 = andii(s0,b)
p03 = a
p = oriii(p01,p02,p03)
print p,g
