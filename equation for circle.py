def distance():
    x = int(raw_input("x "))
    originx = int(raw_input("and it's origin "))
    y = int(raw_input("y "))
    originy = int(raw_input("and it's origin "))
    return ((x-originx)^2+(y-originy)^2)^(1/2)
print distance()
