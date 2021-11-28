import os
import sys
import cv2
import numpy as np
import glob

# Load the image of signature
sign = cv2.imread("digital_sign.png")
h_sign, w_sign, _ = sign.shape

path = str(sys.argv[1])
images = glob.glob(f"{path}/*.*")

for img in images:
    img = cv2.imread(img)
    h_img, w_img, _ = img.shape

    # Get the center of the original image
    center_x = int(w_img / 2)
    center_y = int(h_img / 2)
    left_x = center_x - int(w_sign / 2)
    top_y = center_y - int(h_sign / 2)
    right_x = left_x + w_sign
    bottom_y = top_y + h_sign

    # Get the ROI (Region of Interest)
    roi = img[top_y:bottom_y, left_x:right_x]

    # Add the Logo to the ROI
    result = cv2.addWeighted(roi, 1, sign, 0.5, 0)

    # Replace the ROI on the image
    img[top_y:bottom_y, left_x:right_x] = result

    # Get filename and save the image
    filename = os.path.basename(img)
    cv2.imwrite("images/signed_" + filename, img)

print("Signature added successfully!")
