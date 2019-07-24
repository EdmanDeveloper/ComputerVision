#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2

# Create the haar cascade
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Read the image
image = cv2.imread('Image.jpg')
# Convert images to gray scale 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(gray,1.2,5)

# Print amount of faces detected
print ("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Show emails with faces detected
cv2.imshow("Faces found", image)
cv2.waitKey(0)

