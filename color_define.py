# 顏色辨識
import cv2
import numpy as np 
import time


color = ((32, 114, 47), (139, 255, 255))
lower = np.array(color[0], dtype="uint8")
upper = np.array(color[1], dtype="uint8")
cap = cv2.VideoCapture(0)
n = 1.0
start_time= time.time()
while True:
	ret, frame = cap.read()
	frame = cv2.resize(frame, (400, 225))
	frame = cv2.flip(frame, 1)
	hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	hsv= cv2.GaussianBlur(hsv, (11, 11), 0)
	mask = cv2.inRange(hsv, lower, upper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)
	#out = cv2.bitwise_and(hsv, hsv, mask=mask)
	contours, hierarchy = cv2.findContours(
	mask.copy(),
	cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
	if len(contours) > 0:
		cnt= max(contours, key=cv2.contourArea)
		if cv2.contourArea(cnt) > 100:
			x, y, w, h = cv2.boundingRect(cnt)
			cv2.rectangle(frame, (x-2, y-2), (x+w+4, y+h+4), (0,255,0), 2)
			#cv2.rectangle(hsv, (x-2, y-2), (x+w+4, y+h+4), (0,255,0), 2)
			#cv2.rectangle(out, (x-2, y-2), (x+w+4, y+h+4), (0,255,0), 2)

	#frame = cv2.hconcat([frame, hsv, out])
	cv2.imshow("frame", frame)
	print('FPS: {:4.1f}'.format(n / (time.time() -start_time)))
	n += 1
	if cv2.waitKey(1) == 27:
		cv2.destroyAllWindows()
		break
