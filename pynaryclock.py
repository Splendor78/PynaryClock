import time
import os
from array import *

def main():
    while (1 > 0):
        # Limits re-draw to every new second
        last_sec = time.localtime()
        secs = last_sec
        while last_sec == secs:
            secs = time.localtime()

        # Converts each time element to its own binary char array
        year, month, day, hour, minute, second, weekday, yearday, daylight = secs
                
        seconds_string = "{0:#b}".format(second)
        seconds_string = seconds_string[2:]
        seconds_list = list(seconds_string[::-1])
        
        minutes_string = "{0:#b}".format(minute)
        minutes_string = minutes_string[2:]
        minutes_list = list(minutes_string[::-1])
        
        hours_string = "{0:#b}".format(hour)
        hours_string = hours_string[2:]
        hours_list = list(hours_string[::-1])
        
        # Blank clock list
        clock_list = [
                 ["   ","[ ]"," ","   ","[ ]"," ","   ","[ ]"],
                 ["   ","[ ]"," ","   ","[ ]"," ","   ","[ ]"],
                 ["   ","[ ]"," ","[ ]","[ ]"," ","[ ]","[ ]"],
                 ["[ ]","[ ]"," ","[ ]","[ ]"," ","[ ]","[ ]"]]

        # Adds the current hours to the clock list
        x = 3
        y = 1
        for num in hours_list:
            if num == '1':
                clock_list[x][y] = '[|]'
            else:
                clock_list[x][y] = '[ ]'
            if x == 0:
                y = y - 1
                x = 3
            else:
                x = x - 1

        # Adds the current minutes to the clock list
        x = 3
        y = 4
        for num in minutes_list:
            if num == '1':
                clock_list[x][y] = '[|]'
            else:
                clock_list[x][y] = '[ ]'
            if x == 0:
                y = y - 1
                x = 3
            else:
                x = x - 1

        # Adds the current seconds to the clock list
        x = 3
        y = 7
        for num in seconds_list:
            if num == '1':
                clock_list[x][y] = '[|]'
            else:
                clock_list[x][y] = '[ ]'
            if x == 0:
                y = y - 1
                x = 3
            else:
                x = x - 1

        # Draws the populated clock array
        os.system('cls')
        for i in range (0,4):
            for j in range (0,8):
                print clock_list[i][j],
            print '\n'

        # Adds a human-readable digital clock below the binary clock
        if hour < 10:
            hour1 = '0'
            hour2 = str(hour)
        else:
            hour1 = str(hour)[:1]
            hour2 = str(hour)[-1:]
            
        if minute < 10:
            minute1 = '0'
            minute2 = str(minute)
        else:
            minute1 = str(minute)[:1]
            minute2 = str(minute)[-1:]
            
        if second < 10:
            second1 = '0'
            second2 = str(second)
        else:
            second1 = str(second)[:1]
            second2 = str(second)[-1:]
        
        print '\n ' + hour1 + '   ' + hour2 + '  :  ' + \
        minute1 + '   ' + minute2 + '  :  ' + \
        second1 + '   ' + second2        
            
if __name__ == '__main__':
  main()