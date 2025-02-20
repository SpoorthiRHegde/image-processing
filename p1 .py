# importing libraries
import cv2
import numpy as np

# reading image
#Check to ensure the file exists and the path is correct.
img = cv2.imread("image.png") # Changed file name to match uploaded file.

# Check if the image was loaded correctly
if img is None:
    print("Error: Could not load image. Please check the file path.")
else:
    # Edges
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
              cv2.THRESH_BINARY, 9, 9)

    # Cartoonization
    color = cv2.bilateralFilter(img, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)


    cv2.imshow('p1',img)
    cv2.imshow('p2',edges)
    cv2.imshow('p3',cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
