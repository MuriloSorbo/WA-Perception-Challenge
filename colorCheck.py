import cv2
import numpy as np

def nothing(x):
    pass

FILE_PATH = './red.png'

cv2.namedWindow('marking')

cv2.createTrackbar('H Lower','marking',0,179,nothing)
cv2.createTrackbar('H Higher','marking',179,179,nothing)
cv2.createTrackbar('S Lower','marking',0,255,nothing)
cv2.createTrackbar('S Higher','marking',255,255,nothing)
cv2.createTrackbar('V Lower','marking',0,255,nothing)
cv2.createTrackbar('V Higher','marking',255,255,nothing)


while(1):
    
    img = cv2.imread(FILE_PATH)

    height, width = img.shape[:2]
    img = cv2.resize(img, (width // 3, height // 3))

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    hL = cv2.getTrackbarPos('H Lower','marking')
    hH = cv2.getTrackbarPos('H Higher','marking')
    sL = cv2.getTrackbarPos('S Lower','marking')
    sH = cv2.getTrackbarPos('S Higher','marking')
    vL = cv2.getTrackbarPos('V Lower','marking')
    vH = cv2.getTrackbarPos('V Higher','marking')

    LowerRegion = np.array([hL,sL,vL],np.uint8)
    upperRegion = np.array([hH,sH,vH],np.uint8)

    mask = cv2.inRange(hsv,LowerRegion,upperRegion)

    cv2.imshow("Masking ",mask)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break