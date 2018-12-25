#import datetime
#sha0 = datetime.datetime.now()
#readtime = sha0.find('-')
#readtime
import hashlib
import datetime
from sklearn import svm

def HashedBlock():
    blockFile = open("file.txt","w")
    index = 1
    timestamp = datetime.datetime.now()
    data = ""
    backhashedvariable = (index , timestamp, str(data))
    backhashed = hashlib.sha256(str(backhashedvariable))
    hashed = 0
    for e in range(0,index):
        backhashedvariable = (index , timestamp, str(data))
        backhashed = (hashlib.sha256(str(backhashedvariable)))
        data = raw_input("")
        index += 1
        timestamp = datetime.datetime.now()
        hashedvariable = (index , timestamp, str(data), backhashed)
        hashed = hashlib.sha256(str(hashedvariable))
    blockFile.write(hashed)
    return hashed
        
def hashfinder(sha256):
    #bring all the sha256
    #anaslysis for timestamp
    #analysis for index using last index
    sha0 = sha256
    #bring the sha256
    #decrypt sha256
    #do the first 3 steps just now not to do it before
    pass

hashfinder(HashedBlock())