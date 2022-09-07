import cv2
from cvzone.HandTrackingModule import HandDetector


cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8, maxHands=4)

colorR = (255, 255, 255)  # 方框原始颜色
cx, cy = 100, 100  # 方框原始的中心位置qq
w, h = 200, 200  # 方框的宽(weight)、高(height)

while True:
    colorR = (255, 255, 255)

    success, img = cap.read()
    img = cv2.flip(img, 1)  # 0-垂直翻转，1-水平翻转
    hands, img = detector.findHands(img, flipType=False)

    if hands:

        lmList = hands[0]['lmList']

        distance, _, _ = detector.findDistance(lmList[8], lmList[12], img)  # 食指和中指间的距离

        cursor = lmList[8]  # 食指的位置信息
        if distance < 90:
            if cx - w // 2 < cursor[0] < cx + w // 2 and cy - h // 2 < cursor[1] < cy + h // 2:
                colorR = (0, 255, 0)
                cx, cy = cursor

    # 图像框
    cv2.rectangle(img, (cx - w // 2, cy - h // 2), (cx + w // 2, cy + h // 2),
                  color=colorR, thickness=cv2.FILLED)

    cv2.imshow('Image', img)
    cv2.waitKey(1)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
