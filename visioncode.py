import io
import os
from google.cloud import vision
from google.cloud.vision import types
from io import BytesIO
from PIL import Image
import cv2
import numpy as np

from dotenv import load_dotenv

load_dotenv()

client=vision.ImageAnnotatorClient()

def get_image():
	cap = cv2.VideoCapture(0)
	_, content = cap.read()
	cap.release()
	content = cv2.flip(content,-1)
	_,image=cv2.imencode('.jpg',content)
	image=image.tobytes()
	image = vision.types.Image(content=image)
	return image

def detect_text():
	image = get_image()
	response = client.text_detection(image=image)
	texts = response.text_annotations
	return texts[0].description

detect_text()