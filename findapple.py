from PIL import Image

from sklearn import tree
import numpy as np
#from collections import defaultdict
#by_color = defaultdict(int)
#for pixel in im.getdata():
#    by_color[pixel] += 1
#print by_color
#col = img.convert('RGB').getcolors(maxcolors=1000000)
#col = list(img.getdata(band=0))
red, blue, green = 0,0,0
inp = []
rep = []
for z in range(1,4):
    img = Image.open("apples/apple"+str(z)+".jpg")
    wid,hei = img.size
    for s in range(hei):
        for e in range(wid):
            pixr,pixg,pixb = img.getpixel((e,s))
            if pixr > 0 and pixr < 127:
                red += 1
            if pixg > 0 and pixg < 127:
                green += 1
            if pixb > 0 and pixb < 127:
                blue += 1
    inp.append([red,blue,green])
    rep.append(red)
print z , "apples" ,"with" , inp ,"data"
#print red,'red ',green,'green ',blue,'blue'
clf = tree.DecisionTreeClassifier()
iimg = Image.open(raw_input("Image:"))
wid,hei = iimg.size
for s in range(hei):
    for e in range(wid):
        pixr,g,b = iimg.getpixel((e,s))
        if pixr > 0 and pixr < 127:
            red+=1
cl = clf.fit(inp,rep)
print clf.predict([[red,green,blue]])
