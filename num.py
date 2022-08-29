import cv2
import numpy as np

# img = cv2.imread("roger.jpg")
# print(img.shape)

img = np.empty((300, 300, 3), np.uint8)

for row in range(300):
    for col in range(300):
        img[row][col] = [0, 255, 0]

cv2.imshow("img", img)
cv2.waitKey(0)