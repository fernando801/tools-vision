import numpy as np
import cv2
import argparse
import matplotlib.pyplot as plt
import math
from convolution import convolution
from sobel import metodo_sobel
from Simple import metodo_simple
import urllib.request as urllib

resp = urllib.urlopen("https://drive.google.com/uc?id=1sbsbRr3qWPex9CRM6qMqgzm8MWemJq4i")
image = np.asarray(bytearray(resp.read()), dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_COLOR)

#Metodo Sobel
#El numero debe de ser un numero impar, mayor a 1 (3/5/7 etc)
metodo_sobel(image, 5, verbose=True)

#Metodo Simple
metodo_simple(image,verbose=True)



