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

def gaussian_blur(image, kernel_size, verbose=False):
    if kernel_size % 2 == 0:
        kernel_size += 1

    kernel = gaussian_kernel(kernel_size, sigma=math.sqrt(kernel_size), verbose=verbose)
    return convolution(image, kernel, average=True, verbose=verbose)
