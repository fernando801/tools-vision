import numpy as np
import matplotlib.pyplot as plt
from convolution import convolution

#creates kernel
def gaussian_kernel(K, sigma, verbose=False):
    M = np.zeros((K,K))   #creates an empty matrix for the kernel
    mid = K // 2          #finds the middle of the kernel matrix
    for x in range(K):
        for y in range(K):
            X = x - mid   #this variables set X and Y
            Y = y - mid   #relative to the matrix center
            M[x][y] = (1/(2*np.pi*sigma**2)) * np.e ** (-(X**2+Y**2)/(2*sigma**2)) #calculates kernel values

    if verbose:           #plots the kernel if verbose option is enabled 
        plt.imshow(M, interpolation='none',cmap='gray')
        plt.title("Image")
        plt.show()
    
    return M  #return the kernel matrix

#uses convolution with gaussian kernel
def gaussian_blur(image, kernel_size, sigma, verbose=False):
    kernel = gaussian_kernel(kernel_size, sigma=sigma, verbose=verbose) #gets gaussian smoothing kernel
    conv_img = convolution(image, kernel) #convolutes using gaussian smoothing kernel
    if verbose: #plots convolution matrix if verbose option is enabled
        plt.imshow(conv_img , interpolation='none',cmap='gray')
        plt.title("Gaussian Blur")
        plt.show()
    return conv_img 
