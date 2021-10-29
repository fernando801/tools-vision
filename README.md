# tools-vision
Tool for analyzing and changing an image using different preexisting libraries with Python.

# Teammates
Hlib Korzhynskyy                      A01367464
Jorge Omar López Gemigniani           A01769675
Carlos Eduarod Jiménez Santiago       A01769960
Fernando Reséndiz Bautista            A01769659
Darío Mejía Castillo                  A01769961
Ricardo Alejandro Escalera            A01770360

# Explicación
Simple

Sobel

El Operador Sobel es un operador que enfatiza los bordes de una imagen, teniendo un operador de tipo vertical que enfatiza mas cambios verticales, y un operador horizontal enfatizando cambios horizontales.
El programa primero calcula el kernel usando multiplicacion de matrizes, y luego usa un for loop para hacer un kernel de mayor magnitud a 3.
Tambien en el programa esta la magnitud del gradiente, otro operador enfatizando los bordes de una imagen, pero usando gradientes
La convolucion es una integral que expresa el area de una funcion en el otra. Se usa para ver cuanto es que una funcion esta en otra, y mezcla una funcion con la otra
La convolucion tiene otro significado el cual es el kernel (matriz de convolucion), que tiene como objetivo el afilado, desenfoque, y cambio de una imagen con respecto a las especificaciones de una matriz, que permitira procesar la imagen. Es por eso que el kernel cambia de operador a operador.
https://github.com/adeveloperdiary/blog/tree/master/Computer_Vision/Sobel_Edge_Detection

Gaussian Blur

Mexican Hat

Explicación Código Mexican Hat
Las librearías involucradas en este programa son:Numpy,Cv2,Matplotlib,Math.
Convolution (Una librería la cual nos ayudaría a realizar la convolución una vez tuviéramos el Kernel).
La forma de realizar este código para este método es muy parecida a la forma del código del método “Gaussian Blur”, para evitarnos de problemas, empezamos desde la mitad, tomando a “x” y “y” en el medio de la imagen. Una vez ya teníamos definido el rango que cubrirá “x” y “y” de acuerdo con los parámetros recibidos, en el programa calculamos el valor de nuestro Kernel, basándonos en la forma de la ecuación del método Mexican Hat.
Una vez tenemos el valor del Kernel, viendo las imágenes llegamos a la conclusión de que el resultado se parecía al programa del método “Gaussian Blur”, se parecen, pero no son iguales, para probarlo, en ambos programas imprimimos el Kernel de los mismos para comprobar que el Kernel varía de acuerdo al método. Una vez calculamos nuestro Kernel, realizamos la convolución de la misma imagen con el Kernel y al final solo mostramos nuestra imagen.

Line Detection

Main

El main junta las funciones, Mexican Hat, Line Detection, Gaussian Blir, Sobel y Simple. Esto importa y ejecuta las funciones en el main pasandole parametros a las funciones y 
verbose con un la funcion booleana 'True'
