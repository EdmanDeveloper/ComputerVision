#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import sys

# Load the cascade
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# To capture video from webcam.
video_capture = cv2.VideoCapture(0)

# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = faceCascade.detectMultiScale(gray,1.2,5)

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)
    # Stop if escape key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

