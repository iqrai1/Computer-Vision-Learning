import cv2
import os

# Define the image path
image_path = os.path.join('.', 'data', '1_IM-0001-4001.dcm.png')

# Read the image using OpenCV
img = cv2.imread(image_path)

# Save the image in another format (or after processing)
output_path = os.path.join('.', 'data', 'xray_converted.png')
cv2.imwrite(output_path, img)

cv2.imshow('frame',img)
cv2.waitKey(0)