# 嘗試畫出線條

import numpy as np
import cv2
#建立512x512 的黑色畫布
gc = np.zeros((512, 512, 3), np.uint8)
#用(B, G, R) = (255, 255, 255): 白色填滿畫布
gc.fill(255)
# 從(10, 50) 到(400, 300) 畫條藍色且寬度為5的直線
cv2.line(gc, (10, 50), (400, 300), (255, 0, 0), 5)
cv2.rectangle(gc, (30, 50), (200, 280), (0, 255, 0), 3)
cv2.imshow("draw", gc)
cv2.waitKey(0)
cv2.destroyAllWindows()
