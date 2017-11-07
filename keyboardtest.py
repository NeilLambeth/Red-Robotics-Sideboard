import curses
import time
from sideboard import *
stdscr = curses.initscr()
curses.noecho()
#curses.cbreak()
stdscr.keypad(True)



print("start")
time.sleep(1)

def main(stdscr):
    
    keypress = 0
    up = 0
    stop = 0
    while True:
        
        curses.halfdelay(1)
        c = stdscr.getch()
        #print(c)
        #print("\r")
        
        if c == ord('w'):
            keypress = 1
            print("Forward")
            print("\r")
            stop = 0
            r_motor (100)
            l_motor (100)
            

        elif c == ord('s'):
            keypress = 1
            stop = 0
            print("Backwards")
            print("\r")
            r_motor (-100)
            l_motor (-100)

        elif c == ord('a'):
            keypress = 1
            stop = 0
            print("Left")
            print("\r")
            r_motor (-100)
            l_motor (100)

        elif c == ord('d'):
            keypress = 1
            stop = 0
            print("Right")
            print("\r")
            r_motor (100)
            l_motor (-100)
            
        elif c == ord('x'):
            keypress = 1
            stop = 0
            print("Stop")
            print("\r")
            r_motor (0)
            l_motor (0)    
                            

        if c == -1:
            stop += 1
            #print(stop)
            #print("\r")
            #up = 0

        if keypress == 1 and stop > 4:
            #curses.flash()
            keypress = 0
            stop = 0
            print("Stop----------------------------------------")
            print("\r")
            r_motor (0)
            l_motor (0)
          
curses.wrapper(main)    
            
        
