# Ali Safamansouri
import cv2
import numpy as np

img = np.ones((500, 800), dtype=np.float32)
rows, cols = img.shape
# head
cv2.circle(img, (cols // 2, 50), 40, 0, thickness=2)
# hair
cv2.line(img, (cols // 2, 10), (cols // 2 + 20, 7), 0, 2)
cv2.line(img, (cols // 2, 10), (cols // 2 - 20, 7), 0, 2)
cv2.line(img, (cols // 2, 10), (cols // 2 - 5, 5), 0, 2)
# eye
cv2.ellipse(img, (cols // 2 - 20, 40), axes=(3, 6), angle=10, startAngle=0, endAngle=360, color=0, thickness=-1)
cv2.ellipse(img, (cols // 2 + 20, 40), axes=(3, 6), angle=-10, startAngle=0, endAngle=360, color=0, thickness=-1)
# eyebrow
cv2.ellipse(img, (cols // 2 - 20, 40), axes=(10, 15), angle=0, startAngle=220, endAngle=300, color=0, thickness=2)
cv2.ellipse(img, (cols // 2 + 20, 40), axes=(10, 15), angle=0, startAngle=220, endAngle=300, color=0, thickness=2)
# Mouth
cv2.ellipse(img, (cols // 2, 60), axes=(20, 15), angle=0, startAngle=40, endAngle=150, color=0, thickness=2)
# bust
cv2.line(img, (cols // 2, 50 + 40), (cols // 2 - 5, 90 + 60), 0, 2)
cv2.line(img, (cols // 2 - 5, 90 + 60), (cols // 2 - 5, 150 + 100), 0, 2)
# legs
cv2.line(img, (cols // 2 - 5, 150 + 100), (cols // 2 - 20, 250 + 150), 0, 2)
cv2.ellipse(img, (cols // 2 - 20 - 10, 250 + 150), axes=(10, 3), angle=-10, startAngle=0, endAngle=360, color=0,
            thickness=2)
cv2.line(img, (cols // 2 - 5, 150 + 100), (cols // 2 + 20, 250 + 150), 0, 2)
cv2.ellipse(img, (cols // 2 + 20 + 10, 250 + 150), axes=(10, 3), angle=10, startAngle=0, endAngle=360, color=0,
            thickness=2)
# left hand
cv2.line(img, (cols // 2 - 3, 90 + 40), (cols // 2 + 10, 150 + 100), 0, 2, lineType=cv2.LINE_4)
cv2.ellipse(img, (cols // 2 + 12, 150 + 100 + 10), (3, 10), -10, 0, 360, 0, 2)
# right hand
cv2.line(img, (cols // 2 - 3, 90 + 40), (cols // 2 - 120, 140), 0, 2, lineType=cv2.LINE_4)
cv2.line(img, (cols // 2 - 120, 140), (cols // 2 - 120 - 30, 140 - 90), 0, 2, lineType=cv2.LINE_4)
cv2.ellipse(img, (cols // 2 - 120 - 33, 140 - 90 - 12), (3, 10), -10, 0, 360, 0, 2)

direction = -1
iteration = 1
while True:
    # Clear last move
    cv2.line(img, (cols // 2 - 120, 140), (cols // 2 - 150 + iteration * 2, 50), 255, 2, lineType=cv2.LINE_4)
    cv2.ellipse(img, (cols // 2 - 153 + iteration * 2, 38), (3, 10), -10, 0, 360, 255, 2)
    iteration += direction
    if iteration > 10 or iteration < -10:
        direction *= -1
    # Move hand
    cv2.line(img, (cols // 2 - 120, 140), (cols // 2 - 150 + iteration * 2, 50), 0, 2, lineType=cv2.LINE_4)
    cv2.ellipse(img, (cols // 2 - 153 + iteration * 2, 38), (3, 10), -10, 0, 360, 0, 2)
    cv2.imshow("caricature", img)
    key = cv2.waitKey(40)
    if key == 27 or key == ord('q'):
        break

cv2.destroyAllWindows()
