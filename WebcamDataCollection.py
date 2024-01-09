import cv2
import time
cap=cv2.VideoCapture(1)
num = 0
while True:
    
    
    ret, frame = cap.read()
    
    if ret:
        time.sleep(2)
        cv2.imshow("frame", frame)
        cv2.imwrite("/home/abhilash/Downloads/Webcam1Images/image"+str(num)+".jpg", frame)
        num = num+1
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        
    else:
        break
    
    
cap.release
cv2.destroyAllWindows()
