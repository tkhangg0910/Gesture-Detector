import cv2
from pathlib import Path
import numpy as np
def get_image():
    Class = '8'
    Path('./dataset/'+Class).mkdir(parents=True, exist_ok=True)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    i = 0    
    while True:      
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        if not ret:
            break
        i+= 1
        if i % 5==0:
            cv2.imwrite('./dataset/'+Class+'/'+str(i)+'.png',frame)
      
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('e') or i > 1000:
            break
  
    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
   get_image()

  