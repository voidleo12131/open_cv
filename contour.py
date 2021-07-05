import cv2
image = cv2.imread('tet.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
binary = cv2.threshold(gray,220,255,cv2.THRESH_BINARY_INV)[1]

#mode=cv2.RETR_EXTERNAL
mode = cv2.RETR_TREE

#method = cv2.CHAIN_APPROX_SIMPLE
method = cv2.CHAIN_APPROX_NONE

contours,hierarchy = cv2.findContours(binary,mode,method)
#cv2.drawContours(image,contours,-1,(0,255,128),2)
cv2.drawContours(image,contours,0,(0,0,255),2)
cv2.drawContours(image,contours,1,(153,50,204),2)
cv2.drawContours(image,contours,2,(30,144,255),2)


print (hierarchy)
#for p in contours[0]:
#	cv2.circle(image,tuple(p[0]),5,(0,0,255),2,-1)
cv2.imshow('image',image)
cv2.waitKey(0)
