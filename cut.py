import cv2
import numpy as np
import random

"""
在openCV中
(0,0)代表最左上角的位置
橫軸為x軸
縱軸為y軸
"""

img = cv2.imread("roger.jpg")

new_img = img[:500, :300] #只取得圖片的左上500x300部分
new_img2 = img[:500, 300:500]

cv2.imshow("img", img)
cv2.imshow("new_img", new_img)
cv2.imshow("new_img2", new_img2)
cv2.waitKey(0)