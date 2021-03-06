from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
import cv2
from array import array
import os
from PIL import Image
import sys
import time
#import cv2
#from tts import t2s
import threading

from dotenv import load_dotenv

load_dotenv()

subscription_key=os.environ.get('SUBSCRIPTION_KEY')
endpoint=os.environ.get('ENDPOINT')
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))


def get_image():

    cap = cv2.VideoCapture(0)
    _, content = cap.read()
    cap.release()
    PATH='/home/pi/Desktop/design/event.jpg'
    image = cv2.imwrite(PATH,content)
    return(PATH)

def describe_image():
    filename=get_image()
    local_image = open(filename,'rb')
    description_result = computervision_client.describe_image_in_stream(local_image)
    local_image.close()
    if (len(description_result.captions) == 0):
        print("No description detected.")
    else:
        caption = sorted(description_result.captions,key= lambda i: i.confidence)[-1]
        caption = str(caption.text)
        print(caption)
       # x=threading.Thread(target=t2s,args=(caption,))
       # x.start()
        
def face_feature(filename):
    local_image=open(filename,'rb')
    local_image_features = ["faces"]
    detect_faces_results_local = computervision_client.analyze_image_in_stream(local_image, local_image_features)
    num=len(detect_faces_results_local.faces)
    print("{} faces detected".format(num))
    if num==1:
        caption="I see 1 face which I couldn't recognise"
    else:
        caption="I see {} faces which can't be recognised.I'll list their features".format(num)    
  #  #t2s(caption)
    caption=''
    for face in detect_faces_results_local.faces:
        loop_data="{} of age {} ".format(face.gender, face.age)
        caption+=loop_data
        print(loop_data)
    x=threading.Thread(target=t2s,args=(caption,))
    x.start()