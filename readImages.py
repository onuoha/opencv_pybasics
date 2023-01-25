import numpy as np
import cv2
from matplotlib import pyplot as plt
# Read image in grayscale
img = cv2.imread("images/myImage.jpg", 0)
#cv2.namedWindow('Chido',cv2.WINDOW_AUTOSIZE)
cv2.imshow('My image', img)
k = cv2.waitKey(0) & 0xFF
if k == 27:             # Wait for Esc key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):     # Wait for 's' key to save and exit
    cv2.imwrite('images/panda.png', img)
    cv2.destroyAllWindows()

# Using matplotlib
img2 = cv2.imread("images/panda.png", 1)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # Hides tick values on X and Y axis
plt.show()