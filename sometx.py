"""
s = "I'm your lord and master, from now"
s1 = s[s.find(' '):s.find(' ',s.find(' ')+1)]
s_end = s[s.find(' ',s.find(' ',s.find(' ',s.find(' ',s.find(' ')+1)))):]
def prtstr(s,s2):
	return s + s_end

print prtstr(s1,s_end)


def is_square(matrix):
	for row in matrix:
		if len(row) != len(column):
			print ((("this is not a square matrix!")))
			return False
	return True

a_matrix = [[1,0],
			[0,1]]

another_matrix = [[1,1],
				[0,1],
				[1,2]]

#print is_square(a_matrix)
#print is_square(another_matrix)

def is_identity_matrix(matrix):
	if not is_square(matrix):
		return False
	row_number = 0
	column_number = 0
	for row in matrix:
		print "row_number:", row_number
		print "column_number:", column_number
		column_number = 0
		for column in row:
			if row_number == column_number:
				if column != 1:
					print matrix , False
					return False
			else:
				if column != 0:
					print matrix, False
					return False
			column_number += 1
		row_number += 1
	return True

[a, b, c, d, e]
[x, f, x, x, x]
[x, x, x, x, x]
[x, x, x, x, x]
[x, x, x, x, some_other_point]


test as you go
use print statements to check the state of your program
assert statements can check assumtions


def test():
	def is_square_actual(a_list):
		assert isinstance(a_list,list)
		for row in a_list:
			assert isinstance(row,list)
			if len(row) != len(a_list):
				return False
		return True


	def is_identity_matrix_actual(matrix):
		if not is_square_actual(matrix):
			return False
		for row in range(len(matrix)):
			for column in range(len(matrix[row])):
				if row == column:
					if matrix[row][column] != 1:
						return False
				else:
					if matrix[row][column] != 0:
						return False
		return True

	matrix_list = []
	matrix_list.append([[1,0,0,0],
						[0,1,0,0],
						[0,0,1,0],
						[0,0,0,1]])
	matrix_list.append([[1,0,0],
						[0,1,0],
						[0,0,0]])
	matrix_list.append([[2,0,0],
						[0,2,0],
						[0,0,2]])
	matrix_list.append([[1,0,0,0],
						[0,1,1,0],
						[0,0,0,1]])
	matrix_list.append([[1,0,0,0,0,0,0,0,0]])
	matrix_list.append([[1,0,0,0],
						[0,1,0,2],
						[0,0,1,0],
						[0,0,0,1]])
	for matrix in matrix_list:
		if is_identity_matrix(matrix) != is_identity_matrix_actual(matrix):
			print "Failed Test"
			return False
		print "Passed Tests!"
		return True
	test()


	#begin new code

import sys
	
def remove_html_markup(a):
	tag = False
	quote = False
	out = ""

	for c in a:
		if c == '<':
			tag = True
		elif c == '>':
			tag = False
		elif (c == '"' or c == "'") and tag:
			quote = not quote
		elif not tag:
			out = out + c
	return out

stepping = True
breakpoints = {9: True, 14: True}
def debug(command, my_arg, my_locals):
	global stepping
	global breakpoints

	if command.find(' ') > 0:
		arg = command.split(' ')(1)
	else:
		arg = None

	if command.startswith('s'):
		stepping = True
		return True
	elif command.startswith('c'):
		stepping = False
		return True
#print remove_html_markup("'foo'")
#print remove_html_markup('"foo"')



def traceit(frame, event, arg):
	global stepping
	global breakpoints

	if event == 'Line':
		if stepping or breakpoints.has_key(frame.f_lineno):
			resume = False
			while not resume:
				print event, frame.f_lineno, frame.f.f_code.co_name, frame.f_locals
				command = input_command()
				resume = debug(command, arg, frame.f_locals)

	return traceit

sys.settrace(traceit)

print remove_html_markup('xyz')

sys.settrace(None)



def weekend(d):
	#my code
	if day == 'Saturday' or day == 'Sunday':
        return True
    else:
        return False

print weekend('Mon')
#False
print weekend('sat')
#True
print weekend('July')
#False

####################################

def countdown(n):
    for i in n:
        print str(i)
        i = i - 1
        
    print 'Blastoff!'

countdown(3)

def countdown(n):
    while (n == n and n != 0):
        print n
        n = n - 1
        
    print 'Blastoff!'

countdown(3)


def median(o,t,th):
    i = o + t + th / 2
    if i - t * 2 > i - th * 2 and i - t * 2 < i - o * 2:
        return t
    if i - o * 2 > i - th * 2 and i - o * 2 < i - t * 2:
        return o
    if i - th * 2 > i - o * 2 and i - th * 2 < i - t * 2:
        return th
    if o == t and t == th:
        return t
    if o == t:
        return t
    if o == t and t < th:
        return t
    if th == o and th == t:
        return th
    if th == o and th < t:
        return th
    if th == t and t < o:
        return th






print(median(1,2,3))
#>>> 2

print(median(9,3,6))
#>>> 6

print(median(7,8,7))
#>>> 7

from random import randint

def random_noun():
    strings = ['sofa','llama']
    return strings[randint(0,1)]
    # your code here


from random import randint

def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"
        
def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

def word_transformer(word):
    if word == 'NOUN':
        return random_noun()
    if word == 'VERB':
        return random_verb()
    else:
        return word[0]
    # your code here

list = ['expression','expression',...]

countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

print countries[1][1]

countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21.],
             ['United States','Washington',307]]

dividi = countries[0][2] / countries[2][2]
print dividi


spy = [0,0,7]
agent = spy
spy[2] = agent + 1
# agent[2] = 8


list.append(element)


list+list = [[,],[,]]

len(list)

len([,[[]]]) = 2
len([,]) = 2

p = [1,2]
q=[3,4]
p.append(q)
print p


def pae(p):
	i = 0
	while i != len(p):
		print p[i]
		i = i + 1

pp = [1,2,3,4,5,6,7]
pae(pp)

for name in list:
	block

for e in p:
	print e
 
#e will refer to the element 0 of p at first
#then it will refer to the next elements respectivly

def sum_list(p):
	result = 0
	for e in p:
		result = result + e
	return result

def measure_udacity(s):
    num = 0
    for e in s:
        if e[:][0] == 'U':
            num = num + 1
            
    return num


print measure_udacity(['Dave','Sebastian','Katy'])
#>>> 0

print measure_udacity(['Umika','Umberto'])
#>>> 2

def find_element(p,t):
	i = 0
	while i < len(p):
		if p[i] == t:
			return i
		i = i + 1
	return -1

def find_element(p,t):
	i = 0
	for e in p:
		if e == t:
			return i
		i = i + 1
	return -1

list.index(value)
#it returns an error if value is not on the list
#or it returns the index of the first occurance of this value

value in list
#returns true or false
#reverse it using>
value not in list
not value in list

def find_element(l,v):
    if v in l == True:
        return l.index(v)
    else:
        return -1




#tic_tac_toe_game
#

current_positions = {"top left":" ","top center":" ","top right":" ",
			"center left":" ","center":" ","center right":" ",
			"bottom left":" ", "bottom center": " ","bottom right":" "}
current_player = "X"

some_dictionary = {"a_value" : "x", "some_value" : "y"}
some_string = "Hello {a_value},{some_value}".format(**some_dictionary)
print some_string

def display_board(current_positions):
	board = 
	{top left} | {top center} | {top right}
	----------
	{center left} | {center} | {center right}
	----------
	{bottom left} | {bottom center} | {bottom right}
	.format(**current_positions)
	print board

def user_move(current_positions,current_player):
	possible_moves = []
	user_prompt = "please pick your move from the options below!"
	for position in current_positions:
		if current_positions[position] == " ":
			possible_moves.append(position)
			user_prompt += "\n" + position
		user_prompt += '\n'
		user_choice = raw_input(user_prompt).lower()
		while user_choice not in possible_moves:
			user_choice = raw_input(user_prompt).lower()
		current_positions[user_choice] = current_player
		if current_player == "X":
			current_player == "O"
		else:
			current_player == "X"
		return current_positions,current_player

def is_game_over(current_positions):
	#assuming only one winner
	winners = [["top left","top center","top right"],
				["center left","center","center right"],
				["bottom left","bottom center","bottom right"],
				["top left","center left","bottom left"],
				["top center","center","bottom center"],
				["top right","center right","bottom right"],
				["top left","center","bottom right"],
				["top right","center","bottom left"]]
	for winning_combo in winners:
		possible_winner = current_positions[winning_combo[0]]
		if possible_winner != " ":
			possibly_won = True
			for value in winning_combo:
				if current_positions[value] != possible_winner:
					possibly_won = False
					break
			if possibly_won:
				return possible_winner
	is_draw = False
	for position in current_positions:
		if current_position[position]:
			is_draw = False
			return False
	if is_draw:
		return "Draw!"

def play_game():
	current_positions = {"top left":" ","top center":" ","top right":" ",
			"center left":" ","center":" ","center right":" ",
			"bottom left":" ", "bottom center": " ","bottom right":" "}
	current_player = "X"
	result = False
	while not result:
		display_board(current_positions)
		current_positions,player turn = user_move(current_positions,current_player)
		result = is_game_over(current_positions)
		if result:
			print "GAME OVER"
			print "Result: ",result
play_game()

if y % 4 != 0:
	yt = 'nleap'
if y % 100 != 0:
	yt = 'leap'
if y % 400 != 0:
	yt = 'nleap'
else:
	yt = 'leap'

if y % 4 != 0:
	return False
if y % 100 != 0:
	    return True
if y % 400 != 0:
	return False
else:
	return True

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    ##
    # Your code here. Return True or False
    # Pseudo code for this algorithm is found at
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm
    ##
    if year % 4 != 0:
	    return False
    if year % 100 != 0:
	    return True
    if year % 400 != 0:
	    return False
    else:
	    return True

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    ##
    c = 0
    days = 0
    for daysrefer in daysOfMonths:
        if daysOfMonths[c] == daysrefer:
            days += daysrefer
            break
        else:
            days += daysrefer
            c += 1
    cy = y1
    for ynum in range(y2 - cy):
            if isLeapYear(y1):
                days += 366
                y1+1
            else:
                days += 365
                y1+1
    ##
    if isLeapYear(y2) == False:
        if m2 > m1:
            days += daysOfMonths[m2-1] - (d1 - d2) + daysOfMonths[m2-2]
        if m2 == m1:
            if d2 != d1:
                days += daysOfMonths[m2-1] - d2
    else:
        if m2 > 2:
            days += daysOfMonths[m2-1] - (d1 - d2) + daysOfMonths[m2-2]
        if m2 == m1:
            if d2 != d1:
                days += daysOfMonths[m2-1] - d2
    
    return days
    
print daysBetweenDates(2000, 1, 1, 2017, 1, 1)
print 6253/17

#algorithm
days # of days in month1 - day1
month1 += 1
while month1 < month2:
	days += #of days in month1
	month1 += 1
days += day2
while year1 < year2:
	days += days in year1
#

#simple mechanical algorithm
days = 0
while date1 is before date2:
	date1 = adcance to the next day
	days += 1


def nextDay(year, month, day):
    d = 0
    m = 0
    y = 0
    if month == 12 and day == 30:
        y = year+1
        m = 1
        d = 1
    else:
        if day == 30:
            m = month + 1
            y = year
            d = 1
        else:
            m = month
            y = year
            d = day+1
    # YOUR CODE HERE
    return y,m,d
    
print nextDay(1999,2,30)

def nextDay(year, month, day):
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
	days = 0
	if year1 < year2:	
		days = (year1 - (year2-1)) * 365
		if month2 == month1:
			days += day2
		else:
			if month2 > month1:
				days += day2 + (month2-1)*30
			if month2 < month1:
				days += day2+(month2-1)*30
	else:
		if month2 == month1:
			days += day2
		else:
			days += day2

	return days

print daysBetweenDates(2000,4,1,2001,4,1)

def nextDay(year, month, day):
    
    if isleapyear(year):
        if day < dofl[month-1]:
            return year, month, day + 1
        else:
            if month == 12:
                return year + 1, 1, 1
            else:
                return year, month + 1, 1
    else:
        if day < dofnl[month-1]:
            return year, month, day + 1
        else:
            if month == 12:
                return year + 1, 1, 1
            else:
                return year, month + 1, 1   

import random

random_list = []
list_length = 20

while len(random_list) < list_length:
    random_list.append(random.randint(0,10))

count_list = [0] * 11
index = 0

while index < len(random_list):
    number = random_list[index]
    count_list[number] = count_list[number] + 1
    index = index + 1

print "number | occurrence"
index = 0
num_len = len("number")

while index < len(count_list):
  num_spaces = num_len - len(str(index))
  print " " * num_spaces + str(index) + " | " + str(count_list[index])
  index = index + 1

def product_list(list_of_numbers):
    result = 1
    for e in list_of_numbers:
        result = result * e
    
    return result

def greatest(list_of_numbers):
    great = 0
    index = 0
    el = []
    if list_of_numbers == el:
        return str(0)
    else:
        for e in list_of_numbers:
            if e > list_of_numbers[index]:
                great = e
                index += 1
                return great

ml_string = ml_string.split()
for word in ml_string:
	replacement = word_in_pos(word,parts_of_speech)
if replaement != None:
	word = word.replace(replacement,"corgi")
	replaced.append(word)
	else:
replaced.append word	
replaced = " "
return replaced

#read documentation Python Standrd Library
import time
import webbrowser
print time.ctime() #computer time and date
for e in 3:
	time.sleep(2*60*60)
	webbrowser.open("https://www.youtube.com/watch?v=FwA25yJOQFY")

#external part
#import py_compile
#py_compile.compile("name.py")
#import compileall
#compileall ...


import os

def renameFiles():
	file_list = os.listdir(r"D:\Programs\Sublime Text 3\1mac\Prank")
	print(file_list)
	saved_path = os.getcwd()
	os.chdir(r"D:\Programs\Sublime Text 3\1mac\Prank")
	for file_name in file_list:
		print file_name
		os.rename(file_name,file_name.translate(None,"0123456789"))
renameFiles()


import turtle
def draw_square():
    window =  turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()
    brad.shape("classic")
    brad.color("black")
    brad.speed(2)

    for e in range(4):
        brad.forward(100)
        brad.right(90)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(50)
    angie.forward(150)
    angie.right(90)
    angie.forward(100)
    angie.speed(2)
        
    window.exitonclick()
    
draw_square()

import turtle
def draw_circular_squares():
    window =  turtle.Screen()
    window.bgcolor(0,0,0)
    
    square = turtle.Turtle()
    square.color("#ffffff")
    for e in range(360):
        square.right(-10)
        for e in range(4):
            square.forward(100)
            square.right(90)
draw_circular_squares()

from twilio.rest import TwilioRestClient

account_sid = ""
aut_token = ""
client = TwilioRestClient(account_sid,auth_token)#we call the __init__ function inside of this class

message = client.sms.messages.create(
    body = "Hello, World!",
    to = "",
    from_ = "")
print message.sid


def read_text():
    fileinput = raw_input("Enter File : ")
    quotes = open(fileinput)
    contents_of_file = quotes.read()    
    quotes.close()
    check_profanity(contents_of_file)
    
def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()
    
read_text()

import turtle
isometric = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("black")
isometric.color("black")
isometric.color("red")
isometric.right(-150)
isometric.forward(100)
isometric.right(60)
isometric.forward(100)
isometric.right(60)
isometric.forward(100)
isometric.right(60)
isometric.forward(100)
isometric.right(120)
isometric.forward(100)
isometric.right(60)
isometric.forward(100)
isometric.right(120)
isometric.forward(100)
isometric.right(120)
isometric.forward(200)
isometric.right(-120)
isometric.forward(100)
isometric.right(-60)
isometric.forward(100)
isometric.right(-60)
isometric.right(-60)
isometric.forward(100)
isometric.right(-60)
isometric.forward(400)
f=100000
for e in range(f):
	isometric.forward(0)

"""
#r"1mac/a.jpg"
#r"1mac/b.jpg"
#r"1mac/c.jpg"
#https://www.youtube.com/watch?v=wb49-oV0F78
#Mission: Impossible - Fallout (2018) - Official Trailer - Paramount Pictures
#https://www.youtube.com/watch?v=Qnb2ZdoxbbU
#X-MEN: THE NEW MUTANTS Official Trailer (2018) NEW Marvel X-Men Movie HD
#https://www.youtube.com/watch?v=VW3ecQZVnjI
#Incredibles 2 Official Trailer (Pixar 2018 Animated Film)
import webbrowser

class Movie():
        """This class provides information"""
        VALID_RATINGS = ["G", "PG", "PG-13", "R"]
        
	def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)


