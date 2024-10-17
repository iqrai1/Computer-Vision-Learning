import os
import cv2

# Load the image from the specified path
img = cv2.imread(os.path.join('.', 'data', 'panda.png'))

# Check if the image is loaded properly
if img is None:
    print("Error: Could not load image.")
else:
    # Convert the image to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply binary thresholding to the grayscale image
    ret, thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)

    thresh = cv2.blur(thresh, (10,10))
    ret, thresh = cv2.threshold(thresh, 80, 255, cv2.THRESH_BINARY)

    # Display the original image, grayscale image, and thresholded image
    cv2.imshow('Original Image', img)
    cv2.imshow('Grayscale Image', img_gray)
    cv2.imshow('Threshold Image', thresh)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
