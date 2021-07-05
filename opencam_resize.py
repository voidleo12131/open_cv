#開啟攝影機 並調整大小
import cv2

ESC = 27

cap = cv2.VideoCapture(1)

cv2.namedWindow('video', cv2.WINDOW_NORMAL)

ratio = cap.get(cv2.CAP_PROP_FRAME_WIDTH) / cap.get(cv2.CAP_PROP_FRAME_HEIGHT)



WIDTH = 400

HEIGHT = int(WIDTH / ratio)

while True:

    ret, frame = cap.read()

    frame = cv2.resize(frame, (WIDTH, HEIGHT))

    frame = cv2.flip(frame, 1)

    cv2.imshow('video', frame)

    if cv2.waitKey(1) == ESC:

            cv2.destroyAllWindows()

            break
