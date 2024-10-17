import os
import cv2

# Corrected the path to join the current directory ('.') with the image filename
#img = cv2.imread(os.path.join('.','data', 'freelancer.png'))
img = cv2.imread(os.path.join('.','data', 'bull4.png'))

k_size = 7

img_blur = cv2.blur(img,(k_size,k_size))

img_GUSblur = cv2.GaussianBlur(img,(k_size,k_size),3)

img_medblur = cv2.medianBlur(img,k_size)

# Check if the image is loaded properly
if img is None:
    print("Error: Could not load image.")
else:
    # Display the image in a window
    cv2.imshow('img', img)
    cv2.imshow('img_blur', img_blur)
    cv2.imshow('img_GUSblur', img_GUSblur)
    cv2.imshow('img_medblur', img_medblur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
