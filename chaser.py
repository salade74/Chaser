#!/usr/bin/python

# import libraries
from time import sleep
import RPi.GPIO as GPIO
import sys
import os
import time

#on nettoie l'ecran
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
# now, to clear the screen
cls()

GPIO.setmode(GPIO.BOARD) # set pin numbering system to board or bcm
GPIO.setwarnings(False)

# setup our output pins
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

#define interval delay
arg = int(sys.argv[1])
laps = arg / float(1000)
print ("On affiche largument passe") #Affiche argument
print (sys.argv[1]) #Affiche argument 
print laps  #Affiche argument


#set GPIO LOW
GPIO.output((3,5,11,13,15,19,21,23),GPIO.LOW)

# create an infinite loop
while True:
	
    	# turn leds on
    	print("Output 3 on")
    	GPIO.output(3,GPIO.HIGH)
    	sleep(laps) # sleep laps
    	GPIO.output((3,5,11,13,15,19,21,23),GPIO.LOW)

    	print("Output 5 on")
    	GPIO.output(5,GPIO.HIGH)
    	sleep(laps) # sleep laps
    	GPIO.output((3,5,11,13,15,19,21,23),GPIO.LOW)

    	print("Output 11 on")
    	GPIO.output(11,GPIO.HIGH)
    	sleep(laps) # sleep laps
    	GPIO.output((3,5,11,13,15,19,21,23),GPIO.LOW)

    	print("Output 13 on")
    	GPIO.output(13,GPIO.HIGH)
    	sleep(laps) # sleep laps
    	GPIO.output((3,5,11,13,15,19,21,23),GPIO.LOW)

    	print("Output 15 on")
    	GPIO.output(15,GPIO.HIGH)
    	sleep(laps) # sleep laps
    	GPIO.output((3,5,11,13,15,19,21,23),GPIO.LOW)

    	print("Output 19 on")
    	GPIO.output(19,GPIO.HIGH)
    	sleep(laps) # sleep laps
    	GPIO.output((3,5,11,13,15,19,21,23),GPIO.LOW)

    	print("Output 21 on")
    	GPIO.output(21,GPIO.HIGH)
    	sleep(laps) # sleep laps
    	GPIO.output((3,5,11,13,15,19,21,23),GPIO.LOW)

    	print("Output 23 on")
    	GPIO.output(23,GPIO.HIGH)
    	sleep(laps) # sleep laps
    	GPIO.output((3,5,11,13,15,19,21,23),GPIO.LOW)
    	print("===================")

    	sleep(laps) # sleep laps
