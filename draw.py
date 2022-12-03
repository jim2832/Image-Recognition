import cv2
import numpy as np

img = np.zeros((600, 600, 3), np.uint8) #全為0表示是黑色

"""
img.shape[1]代表圖片的寬度
img.shape[0]代表圖片的高度(長度)
"""

#畫直線
cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (255,255,255), 2) #參數：物件、起始座標、終點座標、顏色、粗度

#畫方型 (cv2.FILLED代表填滿)
cv2.rectangle(img, (100, 100), (200, 200), (0,255,255), 2)
cv2.rectangle(img, (400, 400), (500, 500), (0,255,255), cv2.FILLED) #參數：物件、起始座標、終點座標、顏色、粗度

#畫圓形
cv2.circle(img, (300, 300), 100, (0,0,255), 2) #參數：物件、圓心、半徑、顏色、粗度

#畫橢圓形
cv2.ellipse(img , (300, 300), (50, 100), 45, 0, 360, (255, 0, 0), cv2.FILLED) #參數：物件、(水平半軸,垂直半軸)、旋轉角度、起始角度、終止角度、顏色、粗度

#寫字(不支援中文)
cv2.putText(img, "Hello", (300, 300), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1) #參數：物件、文字、文字左下方的座標、字體、文字大小、顏色、粗度

cv2.imshow("img", img)
cv2.waitKey(0)