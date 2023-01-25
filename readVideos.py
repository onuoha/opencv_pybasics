import cv2
import numpy as np
import sys

cap = cv2.VideoCapture(0)   # 0 (or -1) for Camera1 OR switch to camera2 by passing 1
ok, frame = cap.read()
print(ok)
if not ok:
    print('Could not read video')
    sys.exit()

while True:
    # Capture frame-by-frame
    ok, frame = cap.read()

    # Frame operation
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('My video frame', frame)

    if cv2.waitKey() & 0xFF == 27: # ord('q')... 27 is always for Esc
        break

# Release the capture when all is done
cap.release()
cv2.destroyAllWindows()
