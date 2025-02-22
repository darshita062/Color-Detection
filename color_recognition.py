import cv2
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1200)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,720)
while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    height , width , _ = frame.shape

    cx = int(width/2)
    cy = int(height/2)

    pixel_center = hsv_frame[cy,cx]
    hue_value = pixel_center[0]

    color = "Undefined"
    if hue_value < 2:
        color = "BLACK"
    elif hue_value < 5:
        color = "RED"
    elif hue_value < 22 :
        color = "ORANGE"
    elif hue_value < 33:
        color = "YELLOW"
    elif hue_value < 78:
        color = "GREEN"
    elif hue_value < 131:
        color = "BLUE"
    elif hue_value < 170:
        color = "VOILET"
    else:
        color = "RED"

    pixel_center_bgr = frame[cy,cx]
    b,g,r = int(pixel_center_bgr[0]),int(pixel_center_bgr[1]),int(pixel_center_bgr[2])
    cv2.putText(frame,color,(10,60),1,2,(b,g,r),2)
    cv2.circle(frame,(cx,cy),5,(25,25,25),3)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    #ctrl+c
    if key == 27 or key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
