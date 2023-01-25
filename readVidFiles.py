import cv2
import numpy as np

cap = cv2.VideoCapture("videos/ugoccie.mp4")

if cap.isOpened():
    print(cap.isOpened(),": No problem loading video")
else:
    print(cap.isOpened(), "Problem loading video")

while True:
    ok, frame = cap.read()
    if not ok:
        print("Problem reading frame")
        break
    # Process video frames
    gray_vid = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Ugoccie Video frame", gray_vid)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
    