import cv2
import numpy as np

#創建一個值都為1的二維陣列
kernel = np.ones((3,3), np.uint8)

#讀取圖片
img = cv2.imread("img/foot.jpg")

#把彩色的圖片轉成黑白
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #參數：物件、轉換顏色

#將圖片變模糊(高斯模糊)
blur = cv2.GaussianBlur(img, (15, 15), 100)

#取得圖片的邊緣
canny = cv2.Canny(img, 50, 100)

#將線條膨脹
dilate = cv2.dilate(img, kernel, iterations = 5)

#將線條變細
erode = cv2.erode(img, kernel, iterations = 1)

cv2.imshow("roger", erode)
cv2.waitKey(0)