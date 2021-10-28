import numpy as np
import cv2
import argparse
import matplotlib.pyplot as plt
import math
from convolution import convolution
from sobel import metodo_sobel
import urllib.request as urllib

resp = urllib.urlopen("https://drive.google.com/uc?id=1sbsbRr3qWPex9CRM6qMqgzm8MWemJq4i")
image = np.asarray(bytearray(resp.read()), dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_COLOR)

#Metodo Sobel
filterSobel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
metodo_sobel(image, filter, verbose=True)