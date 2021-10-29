import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import math
from convolution import convolution

def calc_ker(K, sigma, verbose=False):
    KR = np.zeros((K,K))
    mitad = K // 2
    for x in range(K):
        for y in range(K):
            X = x - mitad
            Y = y - mitad
            KR[x][y] = (1/(np.pi*sigma**4)) * ((1-(1/2))*((X**2+Y**2)/sigma**2)) * np.exp( - ((X**2+Y**2)/(2*sigma**2)))
            
    plt.imshow(KR, interpolation='none',cmap='gray')
    plt.title("Kernel - Mexican Hat")
    plt.show()
    return KR


def metodo_MexHat(image, size, sigma, verbose=False):
    sigma2=sigma
    kernel = calc_ker(size, sigma=sigma)
    conv = convolution(image, kernel)
    if verbose:
        plt.imshow(conv, interpolation='none',cmap='gray')
        plt.title("Mexican Hat - Imagen con Convolucion")
        plt.show()
    return conv
