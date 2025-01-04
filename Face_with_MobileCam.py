import cv2
import time

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")

video = cv2.VideoCapture(0)

address = "IP_address"
video.open(address)
# video = cv2.VideoCapture(address)
# time.sleep(2)

while True:
    check,frame = video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    face = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
    for x,y,w,h in face:
        img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),3)

        smile = smile_cascade.detectMultiScale(gray,scaleFactor=1.8,minNeighbors=20)
        for x,y,w,h in smile:
            img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),3)

    cv2.imshow('Face',frame)
    key = cv2.waitKey(1)
    
    if key == ord('q'):
        break
    
video.release()
cv2.distroyAllWindows()
    


# import cv2
# import time

# face_cascade = cv2.CascadeClassifier("/home/kapil/Codes/codes1/haarcascade_frontalface_default.xml")
# smile_cascade = cv2.CascadeClassifier("/home/kapil/Codes/codes1/smile.xml")

# # Open the video capture
# address = "http://192.168.220.136:4747/video"
# video = cv2.VideoCapture(address)

# if not video.isOpened():
#     print("Error: Could not open video stream.")
#     exit()

# while True:
#     check, frame = video.read()
    
#     if not check or frame is None:
#         print("Error: Failed to capture image.")
#         time.sleep(1)  # Wait for a second before retrying
#         continue  # Skip to the next iteration of the loop

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
#     for (x, y, w, h) in face:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 3)

#         smile = smile_cascade.detectMultiScale(gray, scaleFactor=1.8, minNeighbors=20)
#         for (sx, sy, sw, sh) in smile:
#             cv2.rectangle(frame, (sx, sy), (sx + sw, sy + sh), (255, 0, 255), 3)

#     cv2.imshow('gotcha', frame)

#     key = cv2.waitKey(1)
#     if key == ord('q'):
#         break

# video.release()
# cv2.destroyAllWindows()
