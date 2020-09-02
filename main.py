from scene_des import describe_image
from facerecog import match_face
from jitlio import meet
from tts import t2s
import os
import threading

os.system("mpg123 -q Welcome.mp3")

while True:
    print('[+] Listening.....')
    n=int(input())
    if n==1:
        os.system("mpg123 -q face.mp3")
        match_face()
        
    if n==2:
        os.system("mpg123 -q scene.mp3")
        describe_image()

    if n==3:
        os.system("mpg123 -q jitsi.mp3")
        meet()
    
