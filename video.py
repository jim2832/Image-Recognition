#讀取影片
import cv2

#cap = cv2.VideoCapture("my_video.mp4")
cap = cv2.VideoCapture(0) #取得視訊鏡頭的畫面

#顯示影片
while(True):
    ret, frame = cap.read() #回傳兩個變數(有無成功取得下一幀+下一幀的圖片)
    if ret:
        frame = cv2.resize(frame, (0, 0), fx = 3, fy = 3)
        cv2.imshow("video", frame)
    else:
        break
    if cv2.waitKey(10) == ord("q"): #若輸入q則結束影片
        break