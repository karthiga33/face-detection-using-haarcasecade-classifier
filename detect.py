import cv2
import numpy as np


faceCase = cv2.CascadeClassifier(r'C:\Users\Navin\Downloads\haarcasecade.xml')
img = cv2.imread(r'C:\Users\Navin\Downloads\face.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCase.detectMultiScale(gray,1.1,4)
i = 0
for [x,y,w,h] in faces :


    cv2.rectangle(img,(x,y),(x+w, y+h),(255,0,0),2)

num_faces = len(faces)
print("no of faces", num_faces)



cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()