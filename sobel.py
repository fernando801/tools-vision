import numpy as np
import cv2
import argparse
import matplotlib.pyplot as plt
from convolution import convolution
from gaussian_smoothing import gaussian_blur


def metodo_sobel(image, filter, verbose=False):
    new_image_x = convolution(image, filter, verbose)

    if verbose:
        plt.imshow(new_image_x, cmap='gray')
        plt.title("Horizontal Edge")
        plt.show()

    new_image_y = convolution(image, np.flip(filter.T, axis=0), verbose)

    if verbose:
        plt.imshow(new_image_y, cmap='gray')
        plt.title("Vertical Edge")
        plt.show()

    gradient_magnitude = np.sqrt(np.square(new_image_x) + np.square(new_image_y))

    gradient_magnitude *= 255.0 / gradient_magnitude.max()

    if verbose:
        plt.imshow(gradient_magnitude, cmap='gray')
        plt.title("Gradient Magnitude")
        plt.show()

    return gradient_magnitude

path = r'C:\Users\icarus\Downloads\hostnames.png'

image = cv2.imread(path)

filter = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

metodo_sobel(image, filter, verbose=True)