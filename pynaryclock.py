import time
import os
from array import *
from time import strftime, sleep

def main():
    while (1 > 0):
        # Converts hours, minutes, and seconds to their own binary lists
        secs = time.localtime()
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
        x, y = 3, 1
        for num in hours_list:
            clock_list[x][y] = '[|]' if num == '1' else '[ ]'
            y = y - 1 if x == 0 else y
            x = 3 if x == 0 else x - 1

        # Adds the current minutes to the clock list
        x, y = 3, 4
        for num in minutes_list:
            clock_list[x][y] = '[|]' if num == '1' else '[ ]'
            y = y - 1 if x == 0 else y
            x = 3 if x == 0 else x - 1

        # Adds the current seconds to the clock list
        x, y = 3, 7
        for num in seconds_list:
            clock_list[x][y] = '[|]' if num == '1' else '[ ]'
            y = y - 1 if x == 0 else y
            x = 3 if x == 0 else x - 1

        # Draws the populated clock list
        os.system('cls') # Only works in Windows
        for row in clock_list:
            print "".join(row)

        # Adds a human-readable digital clock below the binary clock
        digital = time.strftime("%H%M%S")
        print '\n ' + digital[0] + '  ' + digital[1] + ' : ' + digital[2] + \
        '  ' + digital[3] + ' : ' + digital[4] + '  ' + digital[5]
        
        # Limits re-draw to every new second
        sleep(1)
        
if __name__ == '__main__':
  main()