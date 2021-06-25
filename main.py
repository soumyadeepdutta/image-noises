import numpy as np
import cv2
# import matplotlib.pyplot as plt

from noises import salt_pepper


def mean_filtering(im):
    img = np.ndarray.copy(im)
    w = 2

    for i in range(2, im.shape[0]-2):
        for j in range(2, im.shape[1]-2):
            # print(f'Modifying {i, j}')
            block = im[i-w:i+w+1, j-w:j+w+1]
            m = np.mean(block, dtype=np.float32)
            img[i][j] = int(m)

    return img

# ignore the most white or dark pixels
def weighted_mean(block, tolerance):
    # print(type(block))
    # print(block.ndim)
    # print(block)
    for i in range(block.shape[0]):
        for j in range(block.shape[1]):
            if block[i][j] == 0:
                block[i][j] += tolerance
            elif block[i][j] == 255:
                block[i][j] -= tolerance
    return np.mean(block, dtype=np.float32)


def weighted_mean_filtering(im):
    img = np.ndarray.copy(im)
    w = 2

    for i in range(2, im.shape[0]-2):
        for j in range(2, im.shape[1]-2):
            # print(f'Modifying {i, j}')
            block = im[i-w:i+w+1, j-w:j+w+1]
            m = weighted_mean(block, 40)
            img[i][j] = int(m)

    return img


if __name__ == "__main__":
    # adding salt pepper noise in an image
    source = cv2.imread('./img/sunflower.jpg', cv2.IMREAD_GRAYSCALE)
    sp_noisy = salt_pepper.add_spnoise(source)
    mean_filtered = mean_filtering(sp_noisy)
    weighted_mean_filtered = weighted_mean_filtering(sp_noisy)

    while True:
        cv2.imshow('org', source)
        cv2.imshow('sp_noisy', mean_filtered)
        cv2.imshow('w_sp', weighted_mean_filtering)

        key_pressed = cv2.waitKey(1) & 0xFF
        if key_pressed == ord('q'):
            break

cv2.destroyAllWindows()
exit(1)
