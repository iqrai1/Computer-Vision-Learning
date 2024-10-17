import os
import cv2
import numpy as np

# Load the image from the specified path
img = cv2.imread(os.path.join('.', 'data', 'birds.png'))

# Check if the image is loaded properly
if img is None:
    print("Error: Could not load image.")
else:
    # Convert the image to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply binary inverse thresholding
    ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)

    # Find contours in the thresholded image
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on the original image
    for cnt in contours:
        if cv2.contourArea(cnt) > 200:
            cv2.drawContours(img, [cnt], -1, (0, 255, 0), 1)

    # Display the images
    cv2.imshow('Original Image with Contours', img)
    cv2.imshow('Grayscale Image', img_gray)
    cv2.imshow('Threshold Image', thresh)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
