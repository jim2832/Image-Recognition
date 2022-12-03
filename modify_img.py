import cv2
import numpy as np
import random

"""
在openCV中
(0,0)代表最左上角的位置
橫軸為x軸
縱軸為y軸
"""

"""
img.shape[0] -> 圖片高度
img.shape[1] -> 圖片寬度
img.shape[2] -> RGB
"""

#裁切圖片
def cut_img(img):
    #new_img = img[:500, :300] #只取得圖片的左上500x300部分
    cut_img = img[:500, 300:500]

    return cut_img


#旋轉圖片
def rotate(img):
    (h, w, d) = img.shape
    center = (w//2, h//2)

    #第一個參數為圖片旋轉中心，第二個參數為旋轉角度(逆時針+ 順時針-)，第三個三數為縮放比例
    modify = cv2.getRotationMatrix2D(center, -90, 1) #順時鐘旋轉90度

    #第三個參數變化後的圖片大小
    rotate_img = cv2.warpAffine(img, modify, (w, h))

    return rotate_img


#縮放圖片
def resize(img):
    scale_percent = 50 #縮放比例
    height = int(img.shape[0] * scale_percent /100) #縮放後的高度
    width = int(img.shape[1] * scale_percent /100) #縮放後的寬度
    dim = (width, height) #更新圖片高度和寬度
    
    resize_img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

    return resize_img


img = cv2.imread("img/roger.jpg")
#print(img.shape)

cv2.imshow("img", img)
cv2.imshow("cut_img", cut_img(img))
cv2.imshow("rotate_img", rotate(img))
cv2.imshow("resize_img", resize(img))
cv2.waitKey(0)