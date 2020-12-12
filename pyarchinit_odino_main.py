#######################
### pyArchInit ODINO ##
#########v0.01### #####
#########    ###  #####
#######          ######
######          #######
####            #######
###  #          #######
##  ###        ########
#  ####################
 ######################

import re
import cv2
import pytesseract
from pytesseract import Output
import imutils
import numpy as np


#istanzia pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Legge l'immagine
image = cv2.imread('C:\\Users\\Luca\\Documents\\test_opencv\\test_pyarchinit_odino.jpg')
#image = imutils.resize(image, width=500)

# Convert to Grayscale Image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Removes Noise
gray_image = cv2.bilateralFilter(gray_image, 11, 17, 17)

# Canny Edge Detection
canny_edge = cv2.Canny(gray_image, 0, 2)

# Find contours based on Edges
# The code below needs an - or else you'll get a ValueError: too many values to unpack (expected 2) or a numpy error
contours, new = cv2.findContours(canny_edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:30]

# # Initialize license Plate contour and x,y coordinates
contour_with_license_plate = None
license_plate = None
x =None
y = None
w = None
h = None

# Find the contour with 4 potential corners and create a Region of Interest around it
for contour in contours:
    # Find Perimeter of contour and it should be a closed contour
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
    # This checks if it's a rectangle
    if len(approx) == 4:
        contour_with_license_plate = approx
        x, y, w, h = cv2.boundingRect(contour)
        license_plate = gray_image[y:y + h, x:x + w]
        break


# # approximate_contours = cv2.drawContours(image, [contour_with_license_plate], -1, (0, 255, 0), 3)

# Text Recognition
text = pytesseract.image_to_string(license_plate, lang='ita')
print("Hello Mortal, I am Odin, the God of Runes, and I have answered your prayer. In this photo the SUs are: ")
#test_to_list:
text_lenght = len(text)
print(text[0:text_lenght])





# Draw License Plate and write the Text
image = cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 3)
image = cv2.putText(image, text, (x-100, y-50), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 6, cv2.LINE_AA)

#print("License Plate: ", text)


cv2.imshow("pyARchInit Odino", image)
cv2.waitKey(0)

#taken from https://stackoverflow.com/questions/64530229/how-do-i-get-tesseract-to-read-the-license-plate-in-the-this-python-opencv-proje





img = cv2.imread('C:\\Users\\MYUSER\Documents\\test_opencv\\20170114_110342.jpg', 0)
ret, thresh = cv2.threshold(img, 50, 255, cv2.THRESH_OTSU)
print("Threshold selected : ", ret)
cv2.imwrite("C:\\Users\\Luca\Documents\\test_opencv\\output_image.png", thresh)

kernel = np.array([[-1, -1, -1],
                   [-1, 9, -1],
                   [-1, -1, -1]])

sharpened = cv2.filter2D(thresh, -1, kernel)  # applying the sharpening kernel to the input image & displaying it.
cv2.imshow('Image Sharpening', sharpened)

cv2.waitKey(0)

text = pytesseract.image_to_string("C:\\Users\\Luca\Documents\\test_opencv\\output_image.png", lang='ita')
print("testo selected : ", text)

