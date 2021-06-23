import numpy as np
import cv2
import matplotlib.pyplot as plt


def gaussian(source):
    g_blur = cv2.GaussianBlur(source, (5, 5), 0)
    cv2.imshow('Gaussian', g_blur)

if __name__ == "__main__":
    img = cv2.imread('./img/sunflower.jpg')
    cv2.imshow('Original', img)
    gaussian(img)


    cv2.waitKey(0)
    cv2.destroyAllWindows()
    exit(1)
