import urllib2
bot_chat = open(r"c:/inetpub/wwwroot/chatbot/chat.html","a+")
bot_chat_answ = open(r"c:/inetpub/wwwroot/chatbot/answer.html","a+")
#read_bot_chat = open("chat.txt","r")
#read_bot_chat_answ = open("answer.txt","r")
#file open operations ended
#dictionary = read_bot_chat.readlines() #read chat.append
#answ = read_bot_chat_answ.readlines() #read answer.append
#reading connection localhost
connection = urllib2.urlopen("http://localhost/chatbot/chat.html")
dictionary = connection.read()
dictionary = dictionary.split(",")
connection = urllib2.urlopen("http://localhost/chatbot/answer.html")
answer = connection.read()
answer = answer.split(",")
#initializing ends
def Answer(a):
                print answer[a].decode("utf-8", "replace") #print current index of dictionary list for answ list
def Learn():
                bot_chat.write(","+raw_input("Message:").encode("utf-8", "replace")) #append into chat.append
                bot_chat_answ.write(","+raw_input("Answer:").encode("utf-8", "replace")) #append into answer.append
def Learning(s,ss):
                bot_chat.write(","+s.encode("utf-8", "replace")) #append into chat.append
                bot_chat_answ.write(","+ss.encode("utf-8", "replace")) #append into answer.append
def Guess():
                #<guess the suitable answer here>
                answer = ""
                return answer
def Setuplist(s):
                s = [s]
                for e in range(0,len(s)):
                        if s[e] == ",":
                                s.append(s[:e])
                                s = s[e:]
Setuplist(dictionary)
Setuplist(answer)
#print dictionary
#print answer
print "\nwelcome to ai chatbot module" #intro
print "\nto teach the bot use command 'practice'" #intro and help
print len(dictionary)
print "texts"
print len(answer)
print "answers"

while 1:
                #fix encode of readed files
                #print dictionary.index("hello") #test 01 error!
                ###########
                l = raw_input()
                #comparision_method = [""]
                a = 0
                
                ###########
                #an = "hello" #test 00 worked out!
                #print an.index(raw_input()) #test 00 worked out!
                a = dictionary.index(l) #recieve input's index
                #Learning(raw_input(),Guess())
                if a == 0:#if word is 'practice' execute the following
                        Learn()
                        a = 1 #reset
                elif a == -1:
                    Answer(a)
                    Learning()
                else:
                        Answer(a)

