import numpy as np
import cv2
import os
import pygame
import threading

def thread_callback():
    print("Hello inside Thread")
    pygame.init()
    song = pygame.mixer.Sound('sound.wav')
    clock = pygame.time.Clock()
    song.play()
    while True:
        clock.tick(60)
    pygame.quit()
    


def notice(c):
    if(c>=5):
        thr = threading.Thread(target=thread_callback)
        thr.start()

        

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture('http://192.168.43.1:8080/video')
cap.set(3,640) # set Width
cap.set(4,480) # set Height
while True:
    ret, img = cap.read()
    #img = cv2.flip(img, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,     
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )
    c=0
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        c = c+1
    print(faces)
    cv2.imshow('video',img)

    notice(c)
    

    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
cap.release()
cv2.destroyAllWindows()
