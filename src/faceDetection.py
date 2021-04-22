import numpy as np
import cv2

faceCascade = cv2.CascadeClassifier(
    'Cascades/haarcascade_frontalface_default.xml')  # to load the classifier from directory
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # set Width
cap.set(4, 480)  # set Height
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,  # input grayscale image
        scaleFactor=1.2,  # to specify how much the image is reduced at each image scale
        minNeighbors=5,
        minSize=(20, 20)  # minimum rectangle size to be considered a face
    )
    for (x, y, w, h) in faces: # here we will mark the detected face with a blue rectangle, while x,y,w,h are the
        # coordinates of the detected face
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
    cv2.imshow('Video', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:  # press 'ESC' to quit
        break
cap.release()
cv2.destroyAllWindows()
