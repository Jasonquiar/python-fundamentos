# Texto (string)
# 👇 Estas son tres formas de declarar un string en Python, usando comillas simples, dobles o triples.
comillasSimples = 'Este es un texto'
comillasDobles = "Este es un texto"
comillasTriples = """comillas triples"""

print(comillasSimples)
print(comillasDobles)
print(comillasTriples)

#Números
# 👇 Estas son tres formas de declarar números en Python, usando enteros, flotantes y complejos.
a = 1 # Entero
b = 3.14 # Flotante
c = 5 + 2j # Complejo

print(a)
print(b)
print(c)

# Lista
# Es una colección ordenada y mutable de elementos que cada una tiene un indice asociado. Se pueden modificar, agregar o eliminar elementos de una lista. 
lista = [0,1,2,3,4,5]

# Tupla
# Es una colección ordenada e inmutable de elementos que cada una tiene un indice asociado. No se pueden modificar, agregar o eliminar elementos de una tupla.
tupla = ("a","b","c")

# Diccionario
# Es una coleccion ordenada (Apartir de Python 3.7) y mutable de elementos que cada uno tiene una clave asociada. Se pueden modificar, agregar o eliminar elementos de un diccionario.
diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Conjuntos (sets)
# Es una colección desordenada de elementos únicos. No se pueden modificar, agregar o eliminar elementos de un conjunto
# Los elementos deben ser unicos.
conjunto = {1,1,2,2,3} # Output: {1,2,3}

#booleanos
booleanoVerdadero = True
booleanoFalso = False