from scene_des import describe_image
from jitlio import meet
from tts import t2s
import os
import threading

#os.system("mpg123 -q Welcome.mp3")

while True:
    print('===========LEND YOUR EYES MENU=============\n')
    print('[+] Press Help Button/Say the keyword')
    print('[+] Press Describe Button/Say the keyword')
    n=int(input())
    if n==1:
        print('Help Event Trigerred....')
        meet()
    if n==2:
        print('Event Description Triggered...Capturing Image')
        describe_image()

  
    
