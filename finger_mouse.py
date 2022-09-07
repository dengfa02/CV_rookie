import cv2
from cvzone.HandTrackingModule import HandDetector
import autopy
import pynput


cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=4)

mouse = pynput.mouse.Controller()  # 鼠标

while True:

    success, img = cap.read()
    img = cv2.flip(img, 1)  # 0-垂直翻转，1-水平翻转
    hands, img = detector.findHands(img, flipType=False)

    if hands:

        lmList = hands[0]['lmList']

        cursor = lmList[8]  # 食指的位置信息
        fingers = detector.fingersUp(hands[0])  # 检测哪个手指伸出

        if fingers[1] and not fingers[2]:
            try:
                autopy.mouse.move(*cursor)
            except:
                pass

        distance, _, _ = detector.findDistance(lmList[8], lmList[12], img)  # 食指和中指间的距离

        if distance < 40:
            mouse.click(pynput.mouse.Button.left, count=1)
            mouse.release(pynput.mouse.Button.left)

            # autopy.mouse.toggle(None, True)
            # autopy.mouse.toggle(None, False)
            pass

    cv2.imshow('Image', img)
    cv2.waitKey(1)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
