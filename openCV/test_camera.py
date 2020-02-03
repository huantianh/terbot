import numpy as np
import cv2
import pyrealsense2 as rs


###1st way
gst_str = ('v4l2src device=/dev/video1 ! '                            
		   'video/x-raw, width=(int)1280, height=(int)720 ! '
		   'videoconvert ! appsink')
cap = cv2.VideoCapture(gst_str, cv2.CAP_GSTREAMER)

###2ndway
# ~ cap = cv2.VideoCapture("/dev/video1") # check this
# ~ cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# ~ cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)	

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # choose color
    bgr = frame
    # ~ gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # ~ hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # ~ rgb = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)

    # Display the resulting frame
    cv2.imshow('frame', frame)
   
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
