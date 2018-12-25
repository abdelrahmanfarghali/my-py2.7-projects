#create file and convert it into a list as a variable
file = open(r"D://file","w")
file.write("hello,hi,welcome")
file = open(r"D://file","r")
list = file.read()
list = list.split(",")
print list
