# tools-vision
Tool for analyzing and changing an image using different preexisting libraries with Python.

# Teammates
Hlib Korzhynskyy                      A01367464
Jorge Omar López Gemigniani           A01769675
Carlos Eduardo Jiménez Santiago       A01769960
Fernando Reséndiz Bautista            A01769659
Darío Mejía Castillo                  A01769961
Ricardo Alejandro Escalera            A01770360

# Explicación
Main

El main junta las funciones, Mexican Hat, Line Detection, Gaussian Blir, Sobel y Simple. Esto importa y ejecuta las funciones en el main pasandole parametros a las funciones y 
verbose con un la funcion booleana 'True'. Optamos por crear cada uno de los integrantes un código para un método diferente, nuestra función main se dedica a importar todos los programas para ejecutarlos, al inicio le preguntará el tamaño del kernel deseado y algo a destacar es que el main a partir de un link de google drive accede a la imagen a la que se le aplicaran los kernerls.
https://github.com/adeveloperdiary/blog/tree/master/Computer_Vision/Sobel_Edge_Detection

Simple

El modulo Simple.py que utiliza las librerías de librerías numpy, matplotlib y convolution siendo la última creada por nosotros.
Se implementa en el código la función llamada método_simple el cual se encarga de pedir 3 argumentos correspondientes a image, size, verbose=False para no romper la estructura de los otros Kernel esta funcion nos permite calcular el Kernel mediante la creación de una matriz de unos de tamaño del size que es pedido anterior y previamente el Kernel usado es 1/size^2 y así mediante la convolución y el Kernel ya obtenido despliega los efectos en la imagen.
https://github.com/adeveloperdiary/blog/tree/master/Computer_Vision/Sobel_Edge_Detection

Sobel

El Operador Sobel es un operador que enfatiza los bordes de una imagen, teniendo un operador de tipo vertical que enfatiza mas cambios verticales, y un operador horizontal enfatizando cambios horizontales.
El programa primero calcula el kernel usando multiplicacion de matrizes, y luego usa un for loop para hacer un kernel de mayor magnitud a 3.
Tambien en el programa esta la magnitud del gradiente, otro operador enfatizando los bordes de una imagen, pero usando gradientes
La convolucion es una integral que expresa el area de una funcion en el otra. Se usa para ver cuanto es que una funcion esta en otra, y mezcla una funcion con la otra
La convolucion tiene otro significado el cual es el kernel (matriz de convolucion), que tiene como objetivo el afilado, desenfoque, y cambio de una imagen con respecto a las especificaciones de una matriz, que permitira procesar la imagen. Es por eso que el kernel cambia de operador a operador.
https://github.com/adeveloperdiary/blog/tree/master/Computer_Vision/Sobel_Edge_Detection

Gaussian Blur

El módulo de gaussian_smoothing.py utiliza las librerías numpy, matplotlib y convolution. Cuenta con una función gaussian_kernerl que toma como argumento el tamaño, la desviación estándar y la opción verbose para generar el kernel. Esta función devuelve el kernel como matriz y lo grafica en caso de que la opción verbose sea igual a True. Cuenta con otra función gaussian_blur que toma como parámetro la imagen, el tamaño del kernel, la desviación estándar y la opción verbose para generar la convolución. Esta función devuelve la convolución como matriz y la grafica en caso de que la opción verbose sea igual a True.
https://github.com/adeveloperdiary/blog/tree/master/Computer_Vision/Sobel_Edge_Detection

Mexican Hat

Explicación Código Mexican Hat
Las librearías involucradas en este programa son:Numpy,Cv2,Matplotlib,Math.
Convolution (Una librería la cual nos ayudaría a realizar la convolución una vez tuviéramos el Kernel).
La forma de realizar este código para este método es muy parecida a la forma del código del método “Gaussian Blur”, para evitarnos de problemas, empezamos desde la mitad, tomando a “x” y “y” en el medio de la imagen. Una vez ya teníamos definido el rango que cubrirá “x” y “y” de acuerdo con los parámetros recibidos, en el programa calculamos el valor de nuestro Kernel, basándonos en la forma de la ecuación del método Mexican Hat.
Una vez tenemos el valor del Kernel, viendo las imágenes llegamos a la conclusión de que el resultado se parecía al programa del método “Gaussian Blur”, se parecen, pero no son iguales, para probarlo, en ambos programas imprimimos el Kernel de los mismos para comprobar que el Kernel varía de acuerdo al método. Una vez calculamos nuestro Kernel, realizamos la convolución de la misma imagen con el Kernel y al final solo mostramos nuestra imagen.
https://github.com/adeveloperdiary/blog/tree/master/Computer_Vision/Sobel_Edge_Detection

Line Detection

Para el line detection igualmente se hace uso de las librerías de Python; Numpy, cv2, Matplotlib y convolution; Para line detection se debe establecer previamente un kernel mediante una matriz de 3x3 compuesta únicamente de valores .1 y 2, de los cuales éstos últimos deberán indicar una orientación, la orientación que tengan los valores 2 en la matriz indicarán como kernel que orientación de lineas se busca, es decir, si los valores 2 están alineados en vertical se resaltarán las verticales de la imagen que se reciba y al previamente definir los kernels para las 4 direcciones posibles, se mostrarán 4 imágenes distintas donde será evidente la orientación de las lineas
https://github.com/adeveloperdiary/blog/tree/master/Computer_Vision/Sobel_Edge_Detection
