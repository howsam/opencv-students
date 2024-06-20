import cv2
import numpy as np


img=np.zeros((800,800,3),dtype=np.uint8)
rows,cols,_=img.shape
axis=(300,400)
angle=50
moveAngle=20
backColor=(0,0,255)
moveColor=(0,255,0)
center=(cols//2,rows//2)
fps=5
t=(1000//fps)

cv2.ellipse(img,center,axis,angle,0,360,backColor,thickness=2)
startAngle=angle-moveAngle
endAngle=moveAngle-moveAngle
while True:
    cv2.ellipse(img,center,axis,angle,startAngle,endAngle,backColor,thickness=2)
    startAngle+=moveAngle
    endAngle+=moveAngle
    cv2.ellipse(img,center,axis,angle,startAngle,endAngle,moveColor,thickness=2)
    cv2.imshow("ellips",img)
    key=cv2.waitKey(t)
    if key==27 or key==ord('q'):
        break


cv2.destroyAllWindows()