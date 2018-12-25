def clock_wise(time,minutes):
                    currenthours = time.find(":")
                    if currenthours == 2:
                        clock =[int(time[:2]),int(time[3:])]
                        if clock[1] < 60:
                                clock[1] = clock[1] + minutes
                                print clock[0],":",clock[1]
                        if minutes >= 60:
                                while clock[1] > 60:
                                        clock[1] = clock[1] - 60
                                        clock[0] = clock[0] + 1
                                print clock[0],":",clock[1]
                    elif currenthours == 1:
                        clock =[int(time[:1]),int(time[2:])]
                        if clock[1] < 60:
                                clock[1] = clock[1] + minutes
                                print clock[0],":",clock[1]
                        if minutes >= 60:
                                while clock[1] > 60:
                                        clock[1] = clock[1] - 60
                                        clock[0] = clock[0] + 1
                                print clock[0],":",clock[1]
print "Welcome to Time Calc App"
print "to use the app you first enter current time in format hh:mm"
print "then u enter minutes left for timer to end in format mm"
print "This app is made by abdelrahman kotb aamer and he allows"
print "the use of the program for free."
print "result is always the last time result"
while 1:
        clock_wise(raw_input("Enter Time:"),int(raw_input("Enter Minutes Left:")))
