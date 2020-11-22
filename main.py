from scene_des import describe_image
from jitlio import meet
from tts import t2s
import os
import threading
import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BCM)  
#os.system("mpg123 -q Welcome.mp3")
GPIO.add_event_detect(17,GPIO.FALLING)

GPIO.add_event_detect(17,GPIO.FALLING)

GPIO.add_event_detect(17,GPIO.FALLING)
while True:
    print('===========LEND YOUR EYES MENU=============\n')
    print('[+] Press Help Button')
    print('[+] Press Describe Button')
    print('[+] Press Offline button')
    if GPIO.event_detected(17):
        print('Help Event Trigerred....')
        meet()
    if GPIO.event_detected(17):
        print('Event Description Triggered...Capturing Image')
        describe_image()
    if GPIO.event_detected(17):
        print("US sensors started capturing")    
