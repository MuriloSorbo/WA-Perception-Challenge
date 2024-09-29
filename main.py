import cv2
import numpy as np

FILE_PATH = './red.png' 

srcImg = cv2.imread(FILE_PATH) # read the source Image from file

height, width = srcImg.shape[:2] # get image width and height

# --- Color detection ---------------------------------------
hsv = cv2.cvtColor(srcImg, cv2.COLOR_BGR2HSV) # Convert image to HSV format

LowerRegion = np.array([179,0,220],np.uint8)   # lower hsv values for red color
upperRegion = np.array([179,255,255],np.uint8) # upper hsv values for red color

mask = cv2.inRange(hsv,LowerRegion,upperRegion) # get the mask from the color range 

kernel = np.ones((10, 10), np.uint8)
dilated_mask = cv2.dilate(mask, kernel, iterations=4) # dilate the mask to obtain a better detection
# ---------------------------------------------------------

contours, _ = cv2.findContours(dilated_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Find all the contours of the mask

leftBorder = []
rightBorder = []
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour) # Get the bounding box of the contour

    # Calculate the center of the bounding box
    cX = x + w // 2
    cY = y + h // 2

    if (cX < width / 2):
        leftBorder.append((cX, cY)) # Add point coordinate to the leftBorder array
    else:
        rightBorder.append((cX, cY)) # Add point coordinate to the rightBorder array

# cast to numpy arrays
leftBorder = np.array(leftBorder)
rightBorder = np.array(rightBorder)

# get the linear equation of the function (coeficients a and b)
aL, bL = np.polyfit(leftBorder[:, 1], leftBorder[:, 0], 1)  
aR, bR = np.polyfit(rightBorder[:, 1], rightBorder[:, 0], 1)

# predicts th points for the y position of 10 and for (height - 10)
leftPoint1 = (int(aL * 10 + bL), 10)
leftPoint2 = (int(aL * (height - 10) + bL), height - 10)
rightPoint1 = (int(aR * 10 + bR), 10)
rightPoint2 = (int(aR * (height - 10) + bR), height - 10)

# Draw the two lines
cv2.line(srcImg, leftPoint1, leftPoint2, (0, 0, 255), 2)
cv2.line(srcImg, rightPoint1, rightPoint2, (0, 0, 255), 2)

# Save the image
cv2.imwrite('./out.png', srcImg)