import numpy as np
import cv2
import matplotlib.pyplot as plt
from convolution import convolution
from scipy import signal


def metodo_sobel(image, size, verbose=False):
    #Define los parametros iniciales del kernel de 3x3
    vertical = np.array([[1],[2],[1]])
    horizontal = np.array([[1,0,-1]])
    filter3 = vertical*horizontal
    #Si el kernel es mayor a 3x3, se agrega una funcion que multiplica el kernel para saber el kernel mas grande
    if size == 3:
        filter = filter3
    else:
        filter = filter3
        while size > 3:
            horizontal2 = np.array([[1,2,1]])
            filter = signal.convolve2d(vertical*horizontal2, filter)
            print("Kernel para Metodo Sobel : ")
            print(filter)
            size = size - 2
    
    #Se convulciona con el kernel indicado y se muestra el resultado, en X y en Y
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

    #Se calcula el gradiente
    gradient_magnitude = np.sqrt(np.square(new_image_x) + np.square(new_image_y))

    gradient_magnitude *= 255.0 / gradient_magnitude.max()
    
    if verbose:
        plt.imshow(gradient_magnitude, cmap='gray')
        plt.title("Gradient Magnitude")
        plt.show()

    return gradient_magnitude