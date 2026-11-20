# Todos estos numeros pueden tomar valores positivos, negativos y cero.

x = 1 # Integer
y = 2.5 # Float
z = 1j # Complex (Una parte real y una parte imaginaria)

# Para saber el tipo de dato de una variable, podemos usar la función type().   
print(type(x)) # Imprime: <class 'int'>
print(type(y)) # Imprime: <class 'float'>
print(type(z)) # Imprime: <class 'complex'>

# Recuerda que pueden dar valores positivos, negativos y cero. Por ejemplo:

positivo = 5.5 # Float
negativo = -5.5 # Float
imaginario = -5 - 1j # Complex

# En algunos casos necesitamos cambiar el tipo de dato de una variable, para eso podemos usar las funciones int(), float() y complex().
# A este proceso de cambio se le denominado "casting" o "conversión de tipo". en español le dirian casteo 
# 👇 Aca creamos una variable que denominasmmos xf (x float) y le asignamos el valor de x convertido a float.
xf = float(x)

print(type(xf)) # Imprime: <class 'float'>
print(xf) # Imprime: 1.0 que es el valor de x convertido a float.
# La x antes era 1 como valor entero y ahora es 1.0 como valor flotante.

# 👇 Aca creamos una variable que denominamos  ye (y entero) y le asignamos el valor de y convertido a int.
ye = int(y)

print(type(ye)) # Imprime: <class 'int'>
print(ye) # Imprime: 2 que es el valor de y convertido a int.
# la y antes era 2.5 como valor flotante y ahora es 2 como valor entero.


# Su podemos pasar de entero a flotante y de flotante a entero, pero no podemos pasar de complejo a entero o flotante, ya que el complejo
# tiene una parte imaginaria que no puede ser representada en un entero o flotante.
entero = 5
flotante = 5.5

enteroComplejo = complex(entero) # Crea un número complejo con parte real 5 y parte imaginaria 0
flotanteComplejo = complex(flotante) # Crea un número complejo con parte real 5.5 y parte imaginaria 0

print(enteroComplejo) # Imprime: (5+0j) que es el valor de entero convertido a complejo.
print(type(enteroComplejo)) # Imprime: <class 'complex'>
print(flotanteComplejo) # Imprime: (5.5+0j) que es el valor de flotante convertido a complejo.
print(type(flotanteComplejo)) # Imprime: <class 'complex'>


# Para poder ver numereos aleatorios en Python, podemos usar la libreria random. 
# Esta libreria nos permite generar números aleatorios de diferentes formas, como enteros, flotantes y secuencias aleatorias.
import random

# Usamos randrange() para generar un número aleatorio entre 1 y 10 (sin incluir el 10).
print(random.randrange(1, 10)) # Output número aleatorio entre 1 y 9

