import cv2

img = cv2.imread("roger.jpg")
color = (0, 255, 0)

#轉換成黑白照片 因為人臉辨識不需要用到顏色
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = cv2.CascadeClassifier("face_detect.xml")
face_rect = face.detectMultiScale(gray, 1.1, 4) #物件、縮小倍率、目標要被偵測到幾次才算完成
print("face detected: ", len(face_rect)) #印偵測到幾張臉

#偵測
for (x, y, w, h) in face_rect:
    cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)

cv2.imshow("img", img)
cv2.waitKey(0)