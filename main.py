import numpy as np
import cv2
import argparse
import matplotlib.pyplot as plt
import math
from convolution import convolution
from sobel import metodo_sobel
from Simple import metodo_simple
from gaussian_smoothing import gaussian_blur
import urllib.request as urllib

resp = urllib.urlopen("https://drive.google.com/uc?id=1sbsbRr3qWPex9CRM6qMqgzm8MWemJq4i")
image = np.asarray(bytearray(resp.read()), dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_COLOR)

# def pad_with(vector, pad_width, iaxis, kwargs):
#         pad_value = kwargs.get('padder', 10)
#         vector[:pad_width[0]] = pad_value
#         vector[-pad_width[1]:] = pad_value

# image = np.pad(image, 50, pad_with, padder=0)

# plt.plot(image)

#Metodo Sobel
#El numero debe de ser un numero impar, mayor a 1 (3/5/7 etc)
metodo_sobel(image, 3, verbose=True)

#Metodo Simple
metodo_simple(image,verbose=True)

#Gaussian Blur
gaussian_blur(image, 15, verbose=True)



