import cv2

# cap = cv2.VideoCapture('rstp://admin:dusrn#tlf1@192.168.137.64:554/profile0/media.smp')
cap = cv2.VideoCapture('rtsp://192.168.137.64:554/profile2/media.smp')
# cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if success:
        cv2.imshow('image', frame)

        key = cv2.waitKey(30) & 0xFF


        if(key==27):
            break
    else:
        break

cap.release()

cv2.destroyAllWindows()