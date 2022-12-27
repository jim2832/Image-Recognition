import cv2

img = cv2.imread("img/people.jpg")
color = (0, 255, 0)

#轉換成黑白照片 因為人臉辨識不需要用到顏色
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

eye_classifier = cv2.CascadeClassifier("eye_detect.xml")
eye_rect = eye_classifier.detectMultiScale(gray, 1.5, 5)

print("eye detected: ", len(eye_rect)) #印偵測到幾張臉
print(eye_rect)

#偵測
for (x, y, w, h) in eye_rect:
    cv2.rectangle(img, (x, y), (x+w, y+h), color, 1) #畫出正方形

cv2.imshow("img", img)
#cv2.imwrite("out.jpg", img)
cv2.waitKey(0)