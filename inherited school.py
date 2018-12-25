from school import School
from school import child
listed_items = open("list.txt","r")
item = child()
items = School.item
prices = School.price
quantity = School.qty
generalized = listed_items.read()
generalized = generalized.replace("\n",",")
generalized = generalized.split(",")
for e in range(len(generalized)):
    generalized[e] = int(generalized[e])
    
#not working code it is supposed to arrange items in lists
for e in range(len(generalized)):
    if e+1 % 3 == 0:
        items.append(generalized[e-2])
        prices.append(generalized[e-1])
        quantity.append(generalized[e])
    items.append(generalized[e-2])
    prices.append(generalized[e-1])
    quantity.append(generalized[e])
#end of not working code
def Append():
    listing = open("list.txt","w")
    for e in range(0,len(items)):
        listing.write(str(items[e])+","+str(prices[e])+","+str(quantity[e])+"\n")
def Preview():
    print generalized
    print items
    print prices
    print quantity
