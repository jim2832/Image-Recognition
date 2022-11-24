import cv2
import numpy as np

cap = cv2.VideoCapture(0) #取得視訊鏡頭的畫面

#不同顏色的筆
pen_color_HSV = [[86, 121, 205, 111, 245, 255], 
                [46, 78, 172, 71, 255, 255],
                [22, 70, 214, 31, 255, 255]
                ]

#不同顏色的筆對應的筆尖
pen_color_BGR = [[255, 0, 0],
                [0, 255, 0],
                [0, 255, 255]
                ]

#記錄每個筆畫過的位置和顏色 [x, y, color_ID]
draw_points = []


def find_pen(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #用迴圈跑每個顏色
    for i in range(len(pen_color_HSV)):
        #最大和最小值
        lower = np.array(pen_color_HSV[i][:3])
        upper = np.array(pen_color_HSV[i][3:6])

        mask = cv2.inRange(hsv, lower, upper)

        #過濾顏色
        result = cv2.bitwise_and(img, img, mask = mask)
        pen_x, pen_y = find_contour(mask)
        cv2.circle(img_contour, (pen_x, pen_y), 10, pen_color_BGR[i], cv2.FILLED)

        #先判斷是否有偵測到輪廓
        if(pen_y != -1):
            draw_points.append([pen_x, pen_y, i])

    # cv2.imshow("result", result)


def find_contour(img):
    #檢測輪廓
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = -1, -1, -1, -1
    for cnt in contours:
        cv2.drawContours(img_contour, cnt, -1, (0,0,0), 4) #描邊
        #畫外切正方形
        area = cv2.contourArea(cnt)
        if(area > 500):
            peri = cv2.arcLength(cnt, True)
            vertices = cv2.approxPolyDP(cnt, peri * 0.02, True) #頂點
            x, y, w, h = cv2.boundingRect(vertices) #把每個圖形用方形匡起來 左上x座標、左上y座標、寬度、高度
    return x+w//2, y


#用筆畫圖
def draw(draw_points):
    for point in draw_points:
        cv2.circle(img_contour, (point[0], point[1]), 10, pen_color_BGR[point[2]], cv2.FILLED)


#顯示影片
while(True):
    ret, frame = cap.read() #回傳兩個變數(有無成功取得下一幀->bool + 下一幀的圖片)

    if ret:
        img_contour = frame.copy()
        find_pen(frame)
        draw(draw_points)
        cv2.imshow("contour", img_contour)
    else:
        break

    if cv2.waitKey(1) == ord("q"): #若輸入q則結束影片
        break