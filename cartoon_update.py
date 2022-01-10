# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 21:34:02 2021

@author: faisal
"""

import cv2

camera = cv2.VideoCapture(0)

cv2.namedWindow("image magic")

img_counter = 0

while True:
    return_value, frame = camera.read()
    
    #01. Cartoon Image
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray_blurred = cv2.medianBlur(gray_image, 5)

    edges = cv2.adaptiveThreshold(gray_blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 9)

    color_image = cv2.bilateralFilter(frame, 11, 300, 300)

    cartoon_image = cv2.bitwise_and(color_image, color_image, mask=edges)
    
    cv2.imshow("Cartoon Image", cartoon_image)
    #
    #02. Stylization Image
    stylization_image = cv2.stylization(frame, sigma_s=150, sigma_r=0.25)
    cv2.imshow("Stylization Image", stylization_image)
    #
    #03. Gray Pencil Sketch & Color Pencil Sketch
    sketch_image_gray, sketch_image_color  = cv2.pencilSketch(frame, sigma_s=150, sigma_r=0.05, shade_factor=0.07)
    cv2.imshow("Sketch Grey Image", sketch_image_gray)
    cv2.imshow("Sketch Color Image", sketch_image_color)
    #
    
    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape pressed, closed")
        break
    elif k%256 == 32:
        # SPACE pressed
        image_name = "image_{}.jpg".format(img_counter)
        cv2.imwrite(image_name, frame)
        print("{} written!".format(image_name))
        img_counter += 1
        image_name = "image_{}.jpg".format(img_counter)
        cv2.imwrite(image_name, cartoon_image)
        print("{} written!".format(image_name))
        img_counter += 1
        image_name = "image_{}.jpg".format(img_counter)
        cv2.imwrite(image_name, stylization_image)
        print("{} written!".format(image_name))
        img_counter += 1
        image_name = "image_{}.jpg".format(img_counter)
        cv2.imwrite(image_name, sketch_image_gray)
        print("{} written!".format(image_name))
        img_counter += 1
        image_name = "image_{}.jpg".format(img_counter)
        cv2.imwrite(image_name, sketch_image_color)
        print("{} written!".format(image_name))
        img_counter += 1
        
camera.release()

cv2.destroyAllWindows()