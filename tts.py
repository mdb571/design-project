import os
import sys
from gtts import gTTS

def t2s(text):
	tts = gTTS(text=text,slow=False,lang='en')
	tts.save('/home/rmb571/Documents/projectblind/detect.mp3')
	os.system("mpg123 -q detect.mp3")

