import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import math
from convolution import convolution

#Calculamos nuestro Kernel
def calc_ker(K, sigma, verbose=False):
    #Matriz de ceros
    KR = np.zeros((K,K))
    #Calculamos la mitad
    mitad = K // 2
    #Estblecemos nuestros rangos
    for x in range(K):
        for y in range(K):
            X = x - mitad
            Y = y - mitad
            #Aplicamos la ecuación para el cálculo del Kernel de acuerdo al método utilizado
            KR[x][y] = (1/(np.pi*sigma**4)) * ((1-(1/2))*((X**2+Y**2)/sigma**2)) * np.exp( - ((X**2+Y**2)/(2*sigma**2)))
    #Imprimimos nuestro Kernel para la comprobación de que es diferente        
    plt.imshow(KR, interpolation='none',cmap='gray')
    plt.title("Kernel - Mexican Hat")
    plt.show()
    return KR

#Recibimos nuestro parámetros sobre la imagen, tamaño, sigma y verbose
def metodo_MexHat(image, size, sigma, verbose=False):
    sigma2=sigma
    #Nos movemos a nuestra función para calcular nuestro Kernel, mandando nuestros parámetros
    kernel = calc_ker(size, sigma=sigma)
    #Hacemos la convolución invocando la librería de convolution y su función del mismo nombre
    conv = convolution(image, kernel)
    #Imprimimos
    if verbose:
        plt.imshow(conv, interpolation='none',cmap='gray')
        plt.title("Mexican Hat - Imagen con Convolucion")
        plt.show()
    return conv
