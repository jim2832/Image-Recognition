import cv2
import numpy as np

def empty(v):
    pass

img = cv2.imread('roger.jpg')
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

#控制畫面
cv2.namedWindow("TrackBar")
cv2.resizeWindow("TrackBar", 640, 320) #參數：要設定物件的名稱、寬度、高度

#控制條
cv2.createTrackbar("Hue Min", "TrackBar", 0, 179, empty) #參數：名稱、使用的追蹤條、初始值、最大值、當控制條被改變後要呼叫的函式
cv2.createTrackbar("Hue Max", "TrackBar", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBar", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBar", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBar", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBar", 255, 255, empty)

"""
hsv是另一種表達顏色的方式
用Hue(色調)、Saturation(飽和)、Value(亮度)來表達一個顏色
"""
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#取得控制條上的值
while(True):
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBar")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBar")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBar")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBar")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBar")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBar")
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    #最大和最小值
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(hsv, lower, upper)
    #過濾橘色
    result = cv2.bitwise_and(img, img, mask = mask)

    cv2.imshow("img", img)
    cv2.imshow("hsv", hsv)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)
    cv2.waitKey(1)