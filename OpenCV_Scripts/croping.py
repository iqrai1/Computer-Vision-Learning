import cv2
import os

img = cv2.imread(os.path.join('.', 'data', '1_IM-0001-4001.dcm.png'))

cropped_img = img[320:640,430:840]

print(cropped_img.shape)
