import cv2
import numpy as np


def nothing(x):
    pass


Drawing = False


def draw_circle(event, x, y, flags, param):
    global Drawing, r, g, b
    if event == cv2.EVENT_LBUTTONDOWN:
        Drawing = True
    elif event == cv2.EVENT_MOUSEMOVE:
        if Drawing == True:
            cv2.circle(img, (x, y), 5, (b, g, r), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        Drawing = False
        cv2.circle(img, (x, y), 5, (b, g, r), -1)


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('Paint')
# create trackbars for color change
cv2.createTrackbar('R', 'Paint', 0, 255, nothing)
cv2.createTrackbar('G', 'Paint', 0, 255, nothing)
cv2.createTrackbar('B', 'Paint', 0, 255, nothing)

cv2.setMouseCallback('Paint', draw_circle)

while (1):
    cv2.imshow('Paint', img)
    if cv2.waitKey(5) & 0xFF == 27:
        break
    r = cv2.getTrackbarPos('R', 'Paint')
    g = cv2.getTrackbarPos('G', 'Paint')
    b = cv2.getTrackbarPos('B', 'Paint')

cv2.destroyAllWindows()