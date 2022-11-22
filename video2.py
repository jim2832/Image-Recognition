import cv2

vid = cv2.VideoCapture("my_video.mp4")

while(1):
    ret, frame = vid.read()

    if ret:
        frame = cv2.resize(frame, (0, 0), fx = 1.2, fy = 1.2)
        cv2.imshow("video", frame)
    else:
        break

    if cv2.waitKey(10000) == ord("q"):
        break