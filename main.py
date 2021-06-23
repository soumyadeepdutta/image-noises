import numpy as np
import cv2
import matplotlib.pyplot as plt

from noises import salt_pepper

def gaussian(source):
    g_blur = cv2.GaussianBlur(source, (5, 5), 0)
    cv2.imshow('Gaussian', g_blur)

if __name__ == "__main__":
    img = cv2.imread('./img/sunflower.jpg', cv2.IMREAD_GRAYSCALE)
    image_s = salt_pepper.add_noise(img)
    
    while True:
        # cv2.imshow('Original', img)
        # gaussian(img)
        cv2.imshow('Salt_Pepper', image_s)
        # salt_pepper.add_noise(img)

        key_pressed = cv2.waitKey(1) & 0xFF
        if key_pressed == ord('q'):
            break

cv2.destroyAllWindows()
exit(1)
