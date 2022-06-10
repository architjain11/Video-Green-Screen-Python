import cv2
import numpy as np

video = cv2.VideoCapture('assets\green.mp4')
image = cv2.imread('assets\image.jpg')

while True:
    ret, frame = video.read() #ret is False when some error with video
    frame = cv2.resize(frame, (600, 300))
    image = cv2.resize(image, (600, 300))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # upper and lower hsv value of green colour range to mask
    l_g = np.array([32, 94, 132])
    u_g = np.array([179, 255,255])

    mask = cv2.inRange(hsv, l_g, u_g)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    f = frame-res
    green_screen = np.where(f==0, image, f)

    # output screens
    cv2.imshow("Original Video", frame)
    cv2.imshow("Object Mask", mask)
    cv2.imshow("Background Masked", f)
    cv2.imshow("Final Result", green_screen)

    k = cv2.waitKey(1) #returns unicode value of key pressed
    if k == ord('q'): #ord checks if unicode of 'q' is equal to k
        break

video.release() #release all video resources
cv2.destroyAllWindows()