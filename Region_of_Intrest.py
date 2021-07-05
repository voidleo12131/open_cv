# 處理特定區域
import cv2		
RECT = ((220,20),(370,190))
(left,top),(right,bottom) = RECT	
def roiarea(frame):
  return frame[top:bottom,left:right]	
def replaceroi(frame,roi):
	frame[top:bottom , left:right] = roi
	return frame
cap = cv2. VideoCapture(0)
while True:	
	ret,frame = cap.read()
	frame = cv2.resize(frame,(400,225))
	frame = cv2.flip(frame,1)
	roi = roiarea(frame)
	roi = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
	frame = replaceroi(frame, roi) 	
	
	cv2.rectangle(frame,RECT[0],RECT[1],(0,0,255),2)
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) == 27:
	  cv2.destroyAllWindows()
	  break 
