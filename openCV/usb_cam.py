import numpy as np
import cv2
import pyrealsense2 as rs

WINDOW_NAME = ('USB Camera on JetsonTX2')

gst_str = ('v4l2src device=/dev/video2 ! '                           
		   'video/x-raw, width=(int)1280, height=(int)720 ! '
		   'videoconvert ! appsink')

cap = cv2.VideoCapture(gst_str, cv2.CAP_GSTREAMER)

def read_cam(cap):
	show_help = True
	full_scrn = False
	help_text = ('"Esc" to Quit, "H" to turn off help, "F" to Toggle Fullscreen')
	font = cv2.FONT_HERSHEY_PLAIN
	while True:
	
		# Capture frame-by-frame
		ret, frame = cap.read()

		# choose color
		# ~ bgr = frame
		# ~ gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		# ~ hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		# ~ rgb = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
		
		if show_help:
			cv2.putText(frame, help_text, (11, 20), font,1.0, (32, 32, 32), 4, cv2.LINE_AA)
			cv2.putText(frame, help_text, (10, 20), font,1.0, (240, 240, 240), 1, cv2.LINE_AA)
                        
		# Display the resulting frame
		cv2.imshow(WINDOW_NAME, frame)
	   
		k = cv2.waitKey(5) & 0xFF
		if k == 27:
			break
		elif k == ord('H') or k == ord('h'): # toggle help message
			show_help = not show_help	
		elif k == ord('F') or k == ord('f'): # toggle fullscreen
			full_scrn = not full_scrn
			if full_scrn:
				cv2.setWindowProperty(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
			else:
				cv2.setWindowProperty(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_NORMAL)

def main():
	read_cam(cap)
	cap.release()
	cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
