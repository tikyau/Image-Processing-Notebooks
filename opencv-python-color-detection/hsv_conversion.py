import sys
import cv2

print("Python version: \n" + sys.version)
print("cv2 version: " + cv2.__version__)

#img1 and img2 must be in same size
img1 = cv2.imread('blue.jpg', 1)
hsv1 = cv2.cvtColor(img1, cv2.COLOR_RGB2HSV)
h,s,v = cv2.split(hsv1)
hsv2 = cv2.merge((h,s,v))
img2 = cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB)

cv2.imshow('hsv1',hsv1)

cv2.waitKey(0)
cv2.destroyAllWindow()
