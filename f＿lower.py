# 取顏色的值
from colorfilters import HSVFilter
import cv2 as cv
img = cv.imread('blue.jpg')
img=cv.resize(img,(403,302))
window = HSVFilter(img)
window.show()
print (f'lower:{window.lowerb} upper:{window.upperb}.')


