#finds a fraction in the number
def find_fraction(number):
    number = float(number)
    #if mod/2 less than 0.5 then there is a fraction
    if number % 2 < int(number) + 0.5:
        return 1
#find anything else than a substring
def find_else(string,substring):
    i = 0
    for e in string:
        if string[i] == substring:
            return 0
        else:
            return 1
            pass
        i+=1
    return 0
def bintodec():
    numeric_data = float(raw_input())
    print numeric_data
    for e in int(numeric_data):
            result += numeric_data[e]*2^i
            print e
            i+=1
    if not find_else(str(numeric_data),".") == 1:
        i=0
        for e in range(numeric_data,0):
            result += numeric_data[e]*2^i
            print e
            i+=1
        pass
##    after_the_dot = numeric_data.find(".")
##    an = 0
##    bn = 0
##    result = 0.0
##    if after_the_dot != -1:
##        i = len(numeric_data[:after_the_dot])
##        ii = len(numeric_data[after_the_dot+1:])
##        first = str(reversed(numeric_data[:after_the_dot]))
##        print first
##        second = ((numeric_data[after_the_dot+1:]))
##        for e in range(i):
##                result += 2^(first.find("1"))
##                bn += 1
##                first[:first.find("1")].split("1")
##        for e in range(ii):
##                result += 2^-(second.find("1"))
##                an += 1
##                second[:second.find("1")].split("1")
##        return result
##    else:
##        dotted_null = len(numeric_data)
##        for e in range(dotted_null):
##                result += 2^(numeric_data.find("1"))
##                bn += 1
##                numeric_data[:numeric_data.find("1")+1].split("1")
##        return result
##    while len(numeric_data[after_the_dot+1:]) < len(numeric_data[after_the_dot+1:]):
##        if numeric_data[after_the_dot+e:] == 1:
##            print e
##            result += 2^-an
##        elif numeric_data[after_the_dot+e:] == 0:
##            result += 0
##        an = an + 1
##        e = e + 1
##    while len(numeric_data[:after_the_dot]) < after_the_dot:
##        if numeric_data[:after_the_dot] == 1:
##            print e
##            result += 2^bn
##        elif numeric_data[:after_the_dot] == 0:
##            result += 0
##        bn = bn + 1

print bintodec()
