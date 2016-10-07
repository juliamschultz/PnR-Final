import pigo
import time
import random
from gopigo import *

'''
This class INHERITS your teacher's Pigo class. That means Mr. A can continue to
improve the parent class and it won't overwrite your work.
'''


class GoPiggy(pigo.Pigo):
    # CUSTOM INSTANCE VARIABLES GO HERE. You get the empty self.scan array from Pigo
    # You may want to add a variable to store your default speed
    MIDPOINT = 97
    STOP_DIST = 20

    # CONSTRUCTOR
    def __init__(self):
        print("Piggy has be instantiated!")
        # this method makes sure Piggy is looking forward
        #self.calibrate()
        # let's use an event-driven model, make a handler of sorts to listen for "events"
        while True:
            self.stop()
            self.handler()

    ##### HANDLE IT
    def handler(self):
        ## This is a DICTIONARY, it's a list with custom index values
        # You may change the menu if you'd like
        menu = {"1": ("Navigate forward", self.nav),
                "2": ("Rotate", self.rotate),
                "3": ("Dance", self.dance),
                "4": ("Calibrate servo", self.calibrate),
                "q": ("Quit", quit)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        #
        ans = input("Your selection: ")
        menu.get(ans, [None, error])[1]()

    # A SIMPLE DANCE ALGORITHM
    def dance(self):
        print("Piggy dance")
        ##### WRITE YOUR FIRST PROJECT HERE
        print('Is it safe to dance?')
        for x in range(self.MIDPOINT-20, self.MIDPOINT+20, 5):
            servo(x)
            time.sleep(.1)
        set_speed(150)
        self.encB(10)
        self.encF(5)
        set_speed(225)
        self.encR(20)
        servo(150)
        servo(125)
        self.encL(10)
        self.encF(10)
        servo(40)
        set_speed(75)
        self.encR(10)
        self.encL(4)
        self.encR(4)
        set_speed(225)
        self.encL(20)
        self.encB(25)
        servo(95)
        set_speed(75)
        self.encR(9)
        set_speed(125)
        self.encR(25)
        self.encB(10)
        servo(80)
        servo(120)
        set_speed(175)
        self.encR(50)
        set_speed(225)
        self.encR(75)




    # AUTONOMOUS DRIVING
    def nav(self):
        print("Piggy nav")
        ##### WRITE YOUR FINAL PROJECT HERE


####################################################
############### STATIC FUNCTIONS

def error():
    print('Error in input')


def quit():
    raise SystemExit


####################################################
######## THE ENTIRE APP IS THIS ONE LINE....
g = GoPiggy()
