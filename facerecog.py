import face_recognition
from PIL import Image,ImageDraw
import cv2
import numpy as np
import pickle
import time


def match_face():
    img=cv2.VideoCapture(0)
    frame_count=0
    process_this_frame = True
    while True:
        _, frame = img.read()
        with open('face_encodings.pkl','rb') as f:
            known_faces=pickle.load(f)
        known_face_names = list(known_faces.keys())
        known_face_encodings = np.array(list(known_faces.values()))
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            print('{} faces detected'.format(len(face_encodings)))
            for face_encoding in face_encodings:
                match=face_recognition.compare_faces(known_face_encodings, face_encoding)
                if True in match:
                    match_index=match.index(True)
                    name=known_face_names[match_index]
                    print("{}'s face detected".format(name))
                else:
                    print("New face detetected enter name:")
                    name=input()
                    cv2.imwrite("/home/rmb571/Documents/projectblind/face_data/{}.jpg".format(name),frame)
                    print("New Face added : {}".format(name))
                    frame_count+=50
                    img.set(1, frame_count)
                    process_this_frame=not process_this_frame   
        process_this_frame = not process_this_frame


def bilal_face():
    face_encoding={}
    alister_image=face_recognition.load_image_file('alister.jpg')
    bilal_image=face_recognition.load_image_file('bilal.jpg')
    face_encoding["alister"] = face_recognition.face_encodings(alister_image)[0]

    with open('face_encodings.pkl', 'wb') as f:
        pickle.dump(face_encoding, f)
    print("Alister's face added")
    face_encoding["bilal"] = face_recognition.face_encodings(bilal_image)[0]

    with open('face_encodings.pkl', 'wb') as f:
        pickle.dump(face_encoding, f)
    print("Bilal's face added")

match_face()