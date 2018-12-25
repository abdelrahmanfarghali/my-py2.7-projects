from os import listdir
var = listdir("Programs")
files = open("programs.txt","w")
files.write(str(var))
