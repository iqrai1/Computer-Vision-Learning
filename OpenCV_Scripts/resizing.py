import os
import cv2

img = cv2.imread(os.path.join('.', 'data', '1_IM-0001-4001.dcm.png'))

resize = cv2.resize(img, (440,280))

print(img.shape)
print(resize.shape)

cv2.imshow('img',img)
cv2.imshow('resize',img)

cv2.waitKey(0)