from scene_des import describe_image
from jitlio import meet
#from tts import t2s
from sensor import start_sensor
import os
import threading
import RPi.GPIO as GPIO  
#GPIO.setmode(GPIO.BCM)  
#os.system("mpg123 -q Welcome.mp3")
#GPIO.add_event_detect(13,GPIO.FALLING)

#GPIO.add_event_detect(19,GPIO.FALLING)

#GPIO.add_event_detect(26,GPIO.FALLING)
while True:
    print('===========LEND YOUR EYES MENU=============\n')
    print('[+] Press Help Button')
    print('[+] Press Describe Button')
    print('[+] Press Offline button')
    n=int(input())
    if n==1:
        print('Help Event Trigerred....')
        meet()
    if n==2:
        print('Event Description Triggered...Capturing Image')
        describe_image()
    if n==3:
        print("US sensors started capturing")
        start_sensor()
