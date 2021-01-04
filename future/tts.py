import os
import sys
from gtts import gTTS

def t2s(text):
    tts = gTTS(text=text,slow=False,lang='en')
    tts.save('/home/pi/Desktop/projectblind/Welcome.mp3')
    os.system("mpg123 -q Welcome.mp3")
t2s('Hello there')
