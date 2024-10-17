import os
import cv2
import numpy as np

# Load the image from the specified path
img = cv2.imread(os.path.join('.', 'data', 'player.png'))

# Check if the image is loaded properly
if img is None:
    print("Error: Could not load image.")
else:
    # Apply Canny edge detection
    img_detect = cv2.Canny(img, 100, 200)

    # Dilate the edges to make them thicker
    kernel = np.ones((5, 5), np.uint8)  # Correct kernel definition
    img_edge = cv2.dilate(img_detect, kernel)
    img_erode = cv2.erode(img_edge, kernel)

    # Display the original image, Canny edge detection, and dilated image
    cv2.imshow('Original Image', img)
    cv2.imshow('Edge Detection', img_detect)
    cv2.imshow('Dilated Edges', img_edge)
    cv2.imshow('Dilated Edges', img_erode)
    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
