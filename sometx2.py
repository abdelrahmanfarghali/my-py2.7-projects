Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 4+4
8
>>> l=[4,2,4]
>>> l
[4, 2, 4]
>>> #while loops
>>> #while equality_expression is True:
>>> #give instructions here until equality_expression is False
>>> count = 0
>>> while count < 100:
	#do instructions here
	print count
	count += 1

	
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
>>> # for loops
>>> # for element in list_or_tuple
>>> # do more instructions here
>>> l = [1,4,4,2,3,9,0]
>>> for element in l:
	print element

	
1
4
4
2
3
9
0
>>> range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(100)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> range(25)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
>>> for n in range(100):
	print "hello! the number is " , n
	print "hello! the number is " , n

	
hello! the number is  0
hello! the number is  0
hello! the number is  1
hello! the number is  1
hello! the number is  2
hello! the number is  2
hello! the number is  3
hello! the number is  3
hello! the number is  4
hello! the number is  4
hello! the number is  5
hello! the number is  5
hello! the number is  6
hello! the number is  6
hello! the number is  7
hello! the number is  7
hello! the number is  8
hello! the number is  8
hello! the number is  9
hello! the number is  9
hello! the number is  10
hello! the number is  10
hello! the number is  11
hello! the number is  11
hello! the number is  12
hello! the number is  12
hello! the number is  13
hello! the number is  13
hello! the number is  14
hello! the number is  14
hello! the number is  15
hello! the number is  15
hello! the number is  16
hello! the number is  16
hello! the number is  17
hello! the number is  17
hello! the number is  18
hello! the number is  18
hello! the number is  19
hello! the number is  19
hello! the number is  20
hello! the number is  20
hello! the number is  21
hello! the number is  21
hello! the number is  22
hello! the number is  22
hello! the number is  23
hello! the number is  23
hello! the number is  24
hello! the number is  24
hello! the number is  25
hello! the number is  25
hello! the number is  26
hello! the number is  26
hello! the number is  27
hello! the number is  27
hello! the number is  28
hello! the number is  28
hello! the number is  29
hello! the number is  29
hello! the number is  30
hello! the number is  30
hello! the number is  31
hello! the number is  31
hello! the number is  32
hello! the number is  32
hello! the number is  33
hello! the number is  33
hello! the number is  34
hello! the number is  34
hello! the number is  35
hello! the number is  35
hello! the number is  36
hello! the number is  36
hello! the number is  37
hello! the number is  37
hello! the number is  38
hello! the number is  38
hello! the number is  39
hello! the number is  39
hello! the number is  40
hello! the number is  40
hello! the number is  41
hello! the number is  41
hello! the number is  42
hello! the number is  42
hello! the number is  43
hello! the number is  43
hello! the number is  44
hello! the number is  44
hello! the number is  45
hello! the number is  45
hello! the number is  46
hello! the number is  46
hello! the number is  47
hello! the number is  47
hello! the number is  48
hello! the number is  48
hello! the number is  49
hello! the number is  49
hello! the number is  50
hello! the number is  50
hello! the number is  51
hello! the number is  51
hello! the number is  52
hello! the number is  52
hello! the number is  53
hello! the number is  53
hello! the number is  54
hello! the number is  54
hello! the number is  55
hello! the number is  55
hello! the number is  56
hello! the number is  56
hello! the number is  57
hello! the number is  57
hello! the number is  58
hello! the number is  58
hello! the number is  59
hello! the number is  59
hello! the number is  60
hello! the number is  60
hello! the number is  61
hello! the number is  61
hello! the number is  62
hello! the number is  62
hello! the number is  63
hello! the number is  63
hello! the number is  64
hello! the number is  64
hello! the number is  65
hello! the number is  65
hello! the number is  66
hello! the number is  66
hello! the number is  67
hello! the number is  67
hello! the number is  68
hello! the number is  68
hello! the number is  69
hello! the number is  69
hello! the number is  70
hello! the number is  70
hello! the number is  71
hello! the number is  71
hello! the number is  72
hello! the number is  72
hello! the number is  73
hello! the number is  73
hello! the number is  74
hello! the number is  74
hello! the number is  75
hello! the number is  75
hello! the number is  76
hello! the number is  76
hello! the number is  77
hello! the number is  77
hello! the number is  78
hello! the number is  78
hello! the number is  79
hello! the number is  79
hello! the number is  80
hello! the number is  80
hello! the number is  81
hello! the number is  81
hello! the number is  82
hello! the number is  82
hello! the number is  83
hello! the number is  83
hello! the number is  84
hello! the number is  84
hello! the number is  85
hello! the number is  85
hello! the number is  86
hello! the number is  86
hello! the number is  87
hello! the number is  87
hello! the number is  88
hello! the number is  88
hello! the number is  89
hello! the number is  89
hello! the number is  90
hello! the number is  90
hello! the number is  91
hello! the number is  91
hello! the number is  92
hello! the number is  92
hello! the number is  93
hello! the number is  93
hello! the number is  94
hello! the number is  94
hello! the number is  95
hello! the number is  95
hello! the number is  96
hello! the number is  96
hello! the number is  97
hello! the number is  97
hello! the number is  98
hello! the number is  98
hello! the number is  99
hello! the number is  99
>>> for n in range(100):
	print "hello the number is " + n

	

Traceback (most recent call last):
  File "<pyshell#30>", line 2, in <module>
    print "hello the number is " + n
TypeError: cannot concatenate 'str' and 'int' objects
>>> # create a list of random numbers from 0 to 10 the length of the list is 20 i want a list with 20 randomly generated numbers
>>> import random
>>> random.randint?
SyntaxError: invalid syntax
>>> random.randint(0,10)
3
>>> random.randint(0,10)
7
>>> random.randint(0,10)
6
random.randint(0,10)
>>> 
>>> random.randint(0,10)
7
random.randint(0,10)
>>> 
>>> random.randint(0,10)
8
>>> random.randint(0,10)
9
random.randint(0,10)
>>> 
>>> random.randint(0,10)
3
random.randint(0,10)
>>> 
>>> random.randint(0,10)
10
random.randint(0,10)
>>> 
>>> random.randint(0,10)
2
>>> random.randint(0,10)
8
>>> random_list = []
>>> list_length = 20
>>> output = [7,3,2,3,5,2,1,8,9,9,0]
>>> output
[7, 3, 2, 3, 5, 2, 1, 8, 9, 9, 0]
>>> #random.randint(0,10)x20times
>>> count = 0
>>> while count < list_length:
	random_list.append(random.randint(0,10))
	count += 1

	
>>> random_list
[6, 9, 9, 10, 4, 5, 4, 8, 3, 10, 10, 5, 0, 10, 6, 5, 9, 6, 0, 7]
>>> 
>>> random_list = []
>>> for number in range(list_length):
	random_list.append(random.randint(0,10))

	
>>> random_list
[4, 9, 7, 7, 3, 1, 6, 2, 0, 9, 8, 8, 2, 4, 6, 6, 0, 7, 3, 4]
>>> random_list
[4, 9, 7, 7, 3, 1, 6, 2, 0, 9, 8, 8, 2, 4, 6, 6, 0, 7, 3, 4]
>>> projecteuler.net

Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    projecteuler.net
NameError: name 'projecteuler' is not defined
>>> range(list_length)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> list_length
20
>>> range(list_length) == range(20)
True
>>> #20 is a haqrd-coded value
>>> #define a function and know inputs and outputs
>>> #inputs -> list of 0 to 999
>>> #outputs -> a single number that returns the sum
>>> #modulus -> b % a
>>> 100 % 5
0
>>> 101% 5
1
>>> 101 / 5
20
>>> 101/5.0
20.2
>>> 102%5
2
>>> 103%5
3
>>> 104%5
4
>>> for num in range(10):
	if num % 3 == 0 or num % 5 == 0:
		#add that number to our sum
		e

	

Traceback (most recent call last):
  File "<pyshell#96>", line 4, in <module>
    e
NameError: name 'e' is not defined
>>> sum = 0
>>> for num in range(1000):
	if num % 3 == 0 or num % 5 == 0:
		#add that number to our sum
		sum += num

		
>>> sum
233168
>>> 
>>> 
>>> 
>>> 
