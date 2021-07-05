import cv2
image = cv2.imread('soft.jpg',0)
image = cv2.medianBlur(image,5)
th1 = cv2.adaptiveThreshold(
	image,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
	cv2.THRESH_BINARY,11,2
)
th2 = cv2.adaptiveThreshold(
	image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
	cv2.THRESH_BINARY, 11, 2
)
image = cv2.hconcat([image, th1, th2])
cv2.imshow('image', image)
cv2.waitKey(0)
