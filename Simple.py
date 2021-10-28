import numpy as np
import cv2
import matplotlib.pyplot as plt
from convolution import convolution


def metodo_simple(image, size, verbose=False):
    filtero2=1/(int(size)**2)
    mat=np.ones((size,size))
    filtero = mat*filtero2
    new_image_x = convolution(image,filtero)

    if verbose:
        plt.imshow(new_image_x, cmap='gray')
        plt.title("Simple")
        plt.show()

    return