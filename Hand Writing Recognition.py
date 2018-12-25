#recognition hand writing
from PIL import Image
character_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number_list = ['1','2','3','4','5','6','7','8','9','0']
symbol_list = ['#','@','$','%','^','&','*','(',')','-','=','+','_','!','/']
#h = False
#c = 0
#k = 0
#l = 0
#two = []
#s = open("characters/2.txt","r")
#two.append(s.read())
#s.read().replace("\n",",")
#two[0] = two[0].split(",")
im = Image.open(raw_input("Image:")) # Can be many different formats.
pix = im.load()
#x,y = im.size  # Get the width and hight of the image for iterating over
"""
def readSegment(m,x,y):
    for i in range(y):
        for e in range(x):
            r, b, g = pix[e,i]
            if r < 50 and b < 50 and g < 50:
                pix[x,y] = 0
            else:
                global c
                c = c + 1
                return e, i
                pass
def readLine(x,y):
    for i in range(x):
        for e in range(y):
            r , b , g = pix[i,e]
            if r < 50 and b < 50 and g < 50:
                pix[x,y] = 0
            else:
                global l
                l += 1
                return e, i
                pass
readSegment(readLine(50,50),50,50)
"""
        # Get the RGBA Value of the a pixel of an image
#pix[x,y] = value  # Set the RGBA Value of the image (tuple)
#im.save('alive_parrot.png')  # Save the modified pixels as .png
