"# opencv_pybasics" 
Reference: https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html
echo "# opencv_pybasics" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/onuoha/opencv_pybasics.git
git push -u origin main

…or push an existing repository from the command line
git remote add origin https://github.com/onuoha/opencv_pybasics.git
git branch -M main
git push -u origin main

To save a video, take care of the following:
1. Create an object of a VideoWriter and specify the output file name
2. Specify the FourCC code (4-byte code used to specify the video codec)
3. Specify the number of frames per second (fps)
4. Specify frame size.
5. isColor() flag if True, encoder expects color frame else encoder works with a grayscale frame.

Tutorial 3: Drawing Functions in OpenCV
Goal
Learn to draw different geometric shapes with OpenCV
You will learn these functions : cv2.line(), cv2.circle() , cv2.rectangle(), cv2.ellipse(), cv2.putText() etc.
