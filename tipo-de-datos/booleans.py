# Esta es la forma de declarar variables booleanas en Python, que pueden tomar los valores True o False.
v = True
f = False 

print(v) # imprime True - Verdadero
print(f) # imprime False - Falso

# Utilizamos operadores de comparación tambien se nos obtener valores booleanos,
print(5 > 3) # Verdadero
print(3 > 5) # Falso

print(type(v)) # imprime <class 'bool'>, que nos indica que la variable v es de tipo booleano.

# En caso de que queramos castear un valor a booleano. 
# Podemos utilizar la funcion bool(), que nos permite convertir cualquier valor a su equivalente booleano.
print(bool("Hola Mundo")) # Imprime True, porque el string no esta vacio.
print(bool("")) # Imprime False, porque el string esta vacio.

# True

print(bool("abc")) # Imprime True, porque el string no esta vacio.
print(bool(123)) # Imprime True, porque el numero no es cero.
print(bool(["Manzana", "Pera"])) # Imprime True, porque la lista no esta vacia.

# False

print(bool("")) # Imprime False, porque el string esta vacio.
print(bool(0)) # Imprime False, porque el numero es cero.
print(bool([])) # Imprime False, porque la lista esta vacia.
print(bool(None)) # Imprime False, porque None es un valor nulo.


# En Python, podemos utilizar la funcion isinstance() 
# para verificar si un objeto es una instancia de una clase o de un tipo de dato especifico.

# En este ejemplo, verificamos si la variable x es una instancia de la clase int (entero).
x = 123.5
print(isinstance(x, int)) # Imprime False, porque x es un numero decimal (float) y no un entero (int).

x = 123
print(isinstance(x, int)) # Imprime True, porque x es un entero (int).

# Esto sirve para validar que los datos ingresados por el usuario sean del tipo de dato esperado,
# y evitar errores en el programa.