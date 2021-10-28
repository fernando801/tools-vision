import numpy as np
import cv2
import argparse
import matplotlib.pyplot as plt
import math
from convolution import convolution
from sobel import metodo_sobel
from Simple import metodo_simple
from gaussian_smoothing import gaussian_blur
from metodo_MexicanHat import metodo_MexHat
from line_detection import line_det
import urllib.request as urllib

resp = urllib.urlopen("https://drive.google.com/uc?id=1sbsbRr3qWPex9CRM6qMqgzm8MWemJq4i")
image = np.asarray(bytearray(resp.read()), dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)
def pad_with(vector, pad_width, iaxis, kwargs):
        pad_value = kwargs.get('padder', 10)
        vector[:pad_width[0]] = pad_value
        vector[-pad_width[1]:] = pad_value

image = np.pad(image, 50, pad_with, padder=0)

size=int(input("Longitud del kernel que se desea: "))
if size % 2 == 0:
    size = size + 1
#Metodo Sobel
#El numero debe de ser un numero impar, mayor a 1 (3/5/7 etc)
metodo_sobel(image, size, verbose=True)

#Metodo Simple
metodo_simple(image, size, verbose=True)

#Gaussian Blur
gaussian_blur(image, size, 4, verbose=True)

#Mexican Hat
metodo_MexHat(image, size, 4, verbose=True)

#Line Detection
line_det(image, size, verbose=True)

