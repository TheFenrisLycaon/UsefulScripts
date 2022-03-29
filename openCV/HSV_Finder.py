import cv2
import numpy as np


def empty(x):
    pass


img = cv2.imread('./src/input2/1.jpg')
img = cv2.resize(img, (0, 0), fx=0.1, fy=0.1)

cv2.namedWindow('img')
cv2.createTrackbar('hMin', 'img', 0, 179, empty)
cv2.createTrackbar('sMin', 'img', 0, 255, empty)
cv2.createTrackbar('vMin', 'img', 0, 255, empty)
cv2.createTrackbar('hMax', 'img', 0, 179, empty)
cv2.createTrackbar('sMax', 'img', 0, 255, empty)
cv2.createTrackbar('vMax', 'img', 0, 255, empty)
cv2.setTrackbarPos('hMax', 'img', 179)
cv2.setTrackbarPos('sMax', 'img', 255)
cv2.setTrackbarPos('vMax', 'img', 255)

hMin = sMin = vMin = hMax = sMax = vMax = 0
phMin = psMin = pvMin = phMax = psMax = pvMax = 0
output = img
wait_time = 33

while(1):
    hMin = cv2.getTrackbarPos('hMin', 'img')
    sMin = cv2.getTrackbarPos('sMin', 'img')
    vMin = cv2.getTrackbarPos('vMin', 'img')
    hMax = cv2.getTrackbarPos('hMax', 'img')
    sMax = cv2.getTrackbarPos('sMax', 'img')
    vMax = cv2.getTrackbarPos('vMax', 'img')

    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)

    output = cv2.bitwise_and(img, img, mask=mask)

    if((phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax)):
        print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (
            hMin, sMin, vMin, hMax, sMax, vMax))
        phMin = hMin
        psMin = sMin
        pvMin = vMin
        phMax = hMax
        psMax = sMax
        pvMax = vMax

    cv2.imshow('img', output)

    if cv2.waitKey(wait_time) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
