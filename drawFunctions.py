import numpy as np
import cv2

# Drawing a line
# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Draw a diagonal blue line with thickness of 5px
cv2.line(img, (0,0), (511,511), (0,200,0), 2)
# Draw a rectangle at TRC of img (TLC and BRC x/y-cordinates required)
cv2.rectangle(img, (384,0), (510,128), (255,0,0), 2)
# Draw a circle (center coordinates and radius)
cv2.circle(img, (447,63), 63, (0,0,255), -1) # try 1
cv2.imshow("My image", img)
cv2.waitKey(0)