import cv2

img = cv2.imread("roger.jpg") #讀取圖片

img = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5) #調整大小
cv2.imshow("img", img) #顯示圖片
cv2.waitKey(0) #等待時間後關閉