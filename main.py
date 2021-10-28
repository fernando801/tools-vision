import numpy as np
import cv2
import argparse
import matplotlib.pyplot as plt
import math
from convolution import convolution
from sobel import metodo_sobel


image = cv2.VideoCapture("http://example.com/someimage.jpg")

#Metodo Sobel
filterSobel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
metodo_sobel(image, filter, verbose=True)