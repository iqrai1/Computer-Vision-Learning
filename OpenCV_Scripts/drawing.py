import os
import cv2
import numpy as np

# Load the image from the specified path
img = cv2.imread(os.path.join('.', 'data', 'whiteboard.png'))

# Check if the image is loaded properly
if img is None:
    print("Error: Could not load image.")
else:
    # Draw a line on the image
    img_line = cv2.line(img, (100, 150), (300, 450), (0, 255, 0), 3)

    # Draw a rectangle on the image
    img_rec = cv2.rectangle(img, (200, 350), (300, 450), (0, 0, 255), 3)

    # Draw a circle on the image
    img_circle = cv2.circle(img, (500, 550), 155, (0, 0, 255), 3)

    # Add text to the image (corrected the missing parameters)
    img_text = cv2.putText(img, 'iqra the CV engineer', (800, 450), 
                           cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 2)

    # Display the image with the drawn shapes and text
    cv2.imshow('Image with Shapes and Text', img)
    
    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
