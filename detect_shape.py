import cv2

img = cv2.imread("img/shape.jpg")
img_contour = img.copy() #複製一張圖片給輪廓用

#把圖片轉成黑白 因為檢測時並不需要顏色
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#檢測邊緣
canny = cv2.Canny(img, 150, 200)

#檢測輪廓
contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for cnt in contours:
    cv2.drawContours(img_contour, cnt, -1, (0,0,0), 4) #描邊
    print(cv2.contourArea(cnt)) #輪廓面積
    cv2.arcLength(cnt, True) #輪廓的邊長 #第二個參數代表輪廓是否是閉合的

    #取得頂點
    peri = cv2.arcLength(cnt, True)
    vertices = cv2.approxPolyDP(cnt, peri * 0.02, True)
    print(vertices)

    #畫外切正方形
    area = cv2.contourArea(cnt)
    if(area > 500):
        peri = cv2.arcLength(cnt, True)
        vertices = cv2.approxPolyDP(cnt, peri * 0.02, True) #頂點
        print(vertices)
        x, y, w, h = cv2.boundingRect(vertices) #把每個圖形用方形匡起來 左上x座標、左上y座標、寬度、高度
        cv2.rectangle(img_contour, (x,y), (x+w, y+h), (0,0,0), 1)

        #判斷是哪種形狀
        corners = len(vertices) #頂點的數目
        if(corners == 3): #是三角形
            cv2.putText(img_contour, "triangle", (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0 ,255), 2)
        elif(corners == 4):
            cv2.putText(img_contour, "rectangle", (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0 ,255), 2)
        elif(corners == 5):
            cv2.putText(img_contour, "pentagon", (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0 ,255), 2)
        elif(corners >= 6):
            cv2.putText(img_contour, "circle", (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0 ,255), 2)

cv2.imshow("img", canny)
cv2.imshow("imgContour", img_contour)
cv2.waitKey(0)