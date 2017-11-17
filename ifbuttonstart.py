#! /usr/bin/python
# import libraries
from time import sleep
import RPi.GPIO as GPIO
import sys
import os
import time
from gpiozero import Button
#on nettoie l'ecran
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
# now, to clear the screen
cls()
GPIO.setmode(GPIO.BCM) # set pin numbering system to bcm
GPIO.setwarnings(False)
continue_running=True
#setup GPIO input pins
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# setup our output pins
GPIO.setup(11,GPIO.OUT)
GPIO.setup(9,GPIO.OUT)
#define interval delay
arg = int(sys.argv[1])
laps = arg / float(1000)
print ("On affiche largument passe") #Affiche argument
print (sys.argv[1]) #Affiche argument 
print laps  #Affiche argument
def CLI_A():
	while True :
		print("Output 3 on")
    		GPIO.output(11,GPIO.HIGH)
    		sleep(laps) # sleep laps
    		GPIO.output((11,9),GPIO.LOW)
        	print("Output 3 off")
        	GPIO.output(11,GPIO.LOW)
        	sleep(laps) # sleep laps
        	GPIO.output((9,11),GPIO.LOW)
def CLI_B():
	while True :
        	print("Output 5 on")
        	GPIO.output(9,GPIO.HIGH)
        	sleep(laps) # sleep laps
        	GPIO.output((9,11),GPIO.LOW)
        	print("Output 5 off")
        	GPIO.output(9,GPIO.LOW)
        	sleep(laps) # sleep laps
        	GPIO.output((9,11),GPIO.LOW)
def exit_cleanly():
    global continue_running
    print ("Goodbye, World!")
    continue_running=False
def main():
    global continue_running
    buttonA=Button(18)
    buttonB=Button(23) # Insert the number of the other pin
    buttonA.when_pressed = CLI_A
    buttonB.when_pressed = CLI_B

    # Now loop until you no longer need to
    while(continue_running):
        time.sleep(0.1)
if __name__ == "__main__": main()
