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

GPIO.setmode(GPIO.BOARD) # set pin numbering system to bcm
GPIO.setwarnings(False)

#setup GPIO input pinds
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# setup our output pins
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)

#define interval delay
arg = int(sys.argv[1])
laps = arg / float(1000)
print ("On affiche largument passe") #Affiche argument
print (sys.argv[1]) #Affiche argument 
print laps  #Affiche argument

#set GPIO LOW
GPIO.output((3,5),GPIO.LOW)

# create an infinite loop
while True:
    input_state = GPIO.input(12)
    if input_state == False:
	print('Button A Pressed')
        time.sleep(0.2)

    	print("Output 3 on")
    	GPIO.output(3,GPIO.HIGH)
    	sleep(laps) # sleep laps
    	GPIO.output((3,5),GPIO.LOW)

        print("Output 3 off")
        GPIO.output(3,GPIO.LOW)
        sleep(laps) # sleep laps
        GPIO.output((3,5),GPIO.LOW)

    input_state = GPIO.input(16)
    if input_state == False:
        print('Button B Pressed')
        time.sleep(0.2)

        print("Output 5 on")
        GPIO.output(5,GPIO.HIGH)
        sleep(laps) # sleep laps
        GPIO.output((3,5),GPIO.LOW)

        print("Output 5 off")
        GPIO.output(5,GPIO.LOW)
        sleep(laps) # sleep laps
        GPIO.output((3,5),GPIO.LOW)
