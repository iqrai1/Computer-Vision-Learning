import os
import cv2

# Corrected the path to join the current directory ('.') with the image filename
img = cv2.imread(os.path.join('.','data', 'parrot.png'))

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


img_RGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# Check if the image is loaded properly
if img is None:
    print("Error: Could not load image.")
else:
    # Display the image in a window
    cv2.imshow('img', img)
    cv2.imshow('img_RGB', img_RGB)
    cv2.imshow('img_gray', img_gray)
    cv2.imshow('img_hsv', img_hsv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
