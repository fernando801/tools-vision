import numpy as np
import cv2
import matplotlib.pyplot as plt
from convolution import convolution


def metodo_simple(image, verbose=False):
    LKernel=int(input("Longitud del kernel que se desea: "))
    if LKernel % 2 == 0:
        LKernel = LKernel + 1
    filtero2=1/(int(LKernel)**2)
    mat=np.ones((LKernel,LKernel))
    filtero = mat*filtero2
    
    new_image_x = convolution(image,filtero)

    if verbose:
        plt.imshow(new_image_x, cmap='gray')
        plt.title("Simple")
        plt.show()

    return