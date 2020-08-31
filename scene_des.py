from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time
import cv2
from tts import t2s
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
    image = cv2.imwrite('/home/rmb571/Documents/projectblind/event.jpg',content)
    return('event.jpg')

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
        t2s(caption)
        
    