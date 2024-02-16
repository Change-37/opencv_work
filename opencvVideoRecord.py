# import cv2

# # cap = cv2.VideoCapture('rstp://admin:dusrn#tlf1@192.168.137.64:554/profile0/media.smp')
# cap = cv2.VideoCapture('rtsp://192.168.137.64:554/profile2/media.smp')
# fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
# out = cv2.VideoWriter("output1.avi", fourcc, 20.0, (640, 480))
# # cap = cv2.VideoCapture(0)

# while cap.isOpened():
#     success, frame = cap.read()
#     if success:
#         out.write(frame)
#         cv2.imshow('image', frame)

#         key = cv2.waitKey(30) & 0xFF


#         if(key==27):
#             break
#     else:
#         break

# cap.release()
# out.release()

# cv2.destroyAllWindows()

import cv2
from datetime import datetime

cnt = 0
# 동영상 녹화를 위한 설정
frame_width = 1920
frame_height = 1080
out = cv2.VideoWriter(datetime.now().strftime("%Y-%m-%d %H-%M-%S.avi"),cv2.VideoWriter_fourcc('M','J','P','G'), 15, (frame_width,frame_height))

# 카메라로부터 비디오 가져오기
cap = cv2.VideoCapture('rtsp://192.168.137.64:554/profile2/media.smp')
# cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    if ret:
        # 프레임을 녹화
        out.write(frame)
        # 화면에 프레임 표시
        cnt += 1

        # 'q' 키를 눌러 종료
        if cnt >= 3000:
            break
    else:
        break

# 종료
cap.release()
out.release()
cv2.destroyAllWindows()