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
    STOP_DIST = 30

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
                "5": ("test drive", self.testDrive),
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
        if(self.isClear()):
            print("Let's Dance!!!")
        for x in range(self.MIDPOINT-20, self.MIDPOINT+20, 5):
            servo(x)
            time.sleep(.1)
        if self.isClear():
            set_speed(150)
            self.encR(7)
            self.encL(7)
            self.encR(7)
            self.encL(7)
            set_speed(50)
            self.encB(15)
            set_speed(150)
            self.encF(10)
            servo(80)
            servo(120)
            set_speed(225)
            self.encF(9)
            self.encB(4)
            self.encF(5)
            for x in range(10):
                self.encR(2)
                self.encL(2)
            self.encB(25)
            self.encR(50)
            set_speed(175)
            self.encR(16)
            self.encL(10)
            if self.isClear():
                print("Dance On!!!")
                self.encF(20)
                right_rot()
                time.sleep(1)
                left_rot()
                time.sleep(1)
        self.stop()

    # AUTONOMOUS DRIVING
    def nav(self):
        print("Piggy nav")
        while True:
            while self.isClear():
                # move forward a little bit
                # autonomous driving
                self.testDrive()
            #checking for alternate routes
            answer = self.choosePath()
            #moves left if average is larger
            if answer == "left":
                self.encL(4)
            #moves right if average is larger
            elif answer == "right":
                self.encR(4)

    # Test drive
    def testDrive(self):
        print ("Here I go!")
        fwd()
        while true:
            if us_dist(15) < self.STOP_DIST:
                print("STOP STOP STOP")
                break
            time.sleep(.05)
            print("it's clear, I guess I'll keep going")
        self.stop()
####################################################
############### STATIC FUNCTIONS

def error():
    print('Error in input')


def quit():
    raise SystemExit


####################################################
######## THE ENTIRE APP IS THIS ONE LINE....
g = GoPiggy()
