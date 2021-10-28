import numpy as np
import matplotlib.pyplot as plt
import math
from convolution import convolution


def gaussian_kernel(K, sigma, verbose=False):
    M = np.zeros((K,K))
    mid = K // 2
    for x in range(K):
        for y in range(K):
            X = x - mid
            Y = y - mid
            M[x][y] = (1/(2*np.pi*sigma**2)) * np.e ** (-(X**2+Y**2)/(2*sigma**2))

    if verbose:
        plt.imshow(M, interpolation='none',cmap='gray')
        plt.title("Image")
        plt.show()
    
    return M

def gaussian_blur(image, kernel_size, sigma, verbose=False):
    kernel = gaussian_kernel(kernel_size, sigma=sigma)
    M = convolution(image, kernel, verbose)
    if verbose:
        plt.imshow(M, interpolation='none',cmap='gray')
        plt.title("Gaussian Blur")
        plt.show()
