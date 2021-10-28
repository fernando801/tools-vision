import numpy as np
import cv2
import matplotlib.pyplot as plt
from convolution import convolution


def metodo_simple(image, verbose=False):
   LKernel=int(input("Longitud del kernel que se desea: "))
   pru=LKernel//2
   if pru!=0:
       LKernel=LKernel+1
   filtero2=1/(int(LKernel)**2)
   mat=np.ones((LKernel,LKernel))
   filtero = mat*filtero2
    
   new_image_x = convolution(image,filtero)

   if verbose:
       plt.imshow(new_image_x, cmap='gray')
       plt.title("Horizontal Edge")
       plt.show()

   new_image_y = convolution(image,filtero)

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


