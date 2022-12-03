#coding=utf-8
import cv2
import time
import numpy as np
import mediapipe as mp
from mediapipe import solutions
from PIL import Image, ImageDraw, ImageFont

#印出中文
def cv2ImgAddText(img, text, left, top, textColor=(0, 255, 0), textSize=20):
    if (isinstance(img, np.ndarray)):  #判断是否OpenCV图片类型
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img)
    fontText = ImageFont.truetype(
        "font/simsun.ttc", textSize, encoding="utf-8")
    draw.text((left, top), text, textColor, font=fontText)
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)


cap = cv2.VideoCapture(0) #取得視訊鏡頭
mp_hands = mp.solutions.hands #使用手部追蹤的模型
hands = mp_hands.Hands()

#畫出手部點座標的模型
mp_draw = mp.solutions.drawing_utils
#設定點的樣式(規格)
hand_landmarks_style = mp_draw.DrawingSpec(color = (0, 0, 255), thickness = 5)
#設定線的樣式(規格)
hand_connection_style = mp_draw.DrawingSpec(color = (0, 255, 0), thickness = 10)

#設定FPS的變數
pre_time = 0
cur_time = 0

while(1):
    ret, frame = cap.read()
    if ret:
        frame_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(frame_RGB)
        #print(result.multi_hand_landmarks) #回傳偵測到手上21個點座標
        
        #設定視窗寬度和高度
        frame_height = frame.shape[0]
        frame_width = frame.shape[1]

        if(result.multi_hand_landmarks): #所有手部的點
            for hand_landmarks in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS, hand_landmarks_style, hand_connection_style) #參數：要畫的目的、手部的點、有無連接線、點的樣式、線的樣式
                #印出21個點的座標
                for i, lm in enumerate(hand_landmarks.landmark):
                    x_pos = lm.x * frame_width #真正的x座標
                    y_pos = lm.y * frame_height #真正的y座標

                    #在每個點上加上編號
                    cv2.putText(frame, str(i), (int(x_pos)-25, int(y_pos)+5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,255), 2)

                    #手指最前端
                    # if(i % 4 == 0 and i != 0):
                    #     cv2.circle(frame, (int(x_pos), int(y_pos)), 10, (0,0,255), cv2.FILLED)

                    #大拇指
                    # if(i == 4):
                    #     cv2.putText(frame, "NICE", (int(x_pos)-35, int(y_pos)-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

                    print("第",i+1,"個點\t","x:",int(x_pos)," y:",int(y_pos),"\n")
                    #print(f"第{i+1}個點\tx:{int(x_pos)} y:{int(y_pos)}\n")
                    if(i == 20):
                        print("\n\n\n")
        
        #取得FPS
        cur_time = time.time()
        fps = 1/(cur_time - pre_time)
        pre_time = cur_time
        cv2.putText(frame, f"FPS: {int(fps)}", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 3)

        cv2.imshow("frame", frame)

    if cv2.waitKey(1) == ord("q"):
        break