import RPi.GPIO as GPIO
import time
from datetime import datetime
import os

# GPIO setup
GPIO.setmode (GPIO.BCM)
GPIO.setwarnings(False)

# setup gpio for echo & trig
def start_sensor():
    echopin = [4,24,18]
    trigpin = [3,21,15]
    motrpin=[14,2]

    for j in range(3):
        GPIO.setup(trigpin[j], GPIO.OUT)
        GPIO.setup(echopin[j], GPIO.IN)
        if j<2:
            GPIO.setup(motrpin[j],GPIO.OUT)
    try:
        # main loop
        while True:
            # get distances and assemble data line for writing 
            for j in range(3):

                distance = ping(echopin[j], trigpin[j])
                if j==2 and distance<20:
                    GPIO.output(motrpin[j-1], True)
                    GPIO.output(motrpin[j-2], True)
                if j!=2 and distance<20:
                    GPIO.output(motrpin[j], True)
                elif distance>20 and j==2:
                    GPIO.output(motrpin[j-1], False)
                    GPIO.output(motrpin[j-2], False)
                print ("sensor", j+1,": ",distance,"cm")
                


        
    except KeyboardInterrupt:
        print("Exiting..")
        GPIO.cleanup()  
      
  
# Get reading from HC-SR04   
def ping(echo, trig):
    
    GPIO.output(trig, False)
    # Allow module to settle
    time.sleep(0.5)
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)
    pulse_start = time.time()

    # save StartTime
    while GPIO.input(echo) == 0:
        pulse_start = time.time()
        

    # save time of arrival
    while GPIO.input(echo) == 1:
        pulse_end = time.time()
        

    # time difference between start and arrival
    pulse_duration = pulse_end - pulse_start
    # mutiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = pulse_duration * 17150
    
    distance = round(distance, 2)
    
    return distance

