import numpy as np
import matplotlib.pyplot as plt
import skimage
import cv2


def q52(image, n):
    profile = skimage.measure.profile_line(image, (n, 0), (n, image.shape[0]))
    plt.plot(profile)
    plt.show()


image = cv2.imread("cameraman.tif")
n = int(input('please enter a number:'))
q52(image, n)
