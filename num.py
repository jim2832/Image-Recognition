import cv2
import numpy as np
import random
SIZE = 300

img = cv2.imread("roger.jpg")
# print(img.shape)

# img = np.empty((SIZE, SIZE, 3), np.uint8) #圖片陣列
#img = cv2.resize(img, (0, 0), fx = 3, fy = 3)
# print(type(img)) -> <class 'numpy.ndarray'>

for row in range(SIZE):
    for col in range(SIZE):
    # for col in range(img.shape[1]):
        #img[row][col] = [0,255,0]
        img[row][col] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)] #list內代表BGR(藍、綠、紅)三個元素

cv2.imshow("img", img)
cv2.waitKey(0)