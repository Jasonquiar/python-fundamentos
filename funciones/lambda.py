# Lambda es una función pequeña y anónima que puede tener muchos argumentos pero sólo una expresión

# Sintaxis lambda argumentos : expresión

x = lambda a: a + 10

print(x(5)) # Devuelve 15  

y = lambda a, b: a + b
print(y(2,3)) # Devuelve 5  

# Nota: la expresion puede recibir varios argumentos

# Ejemplo: usar una lambda dentro de una función normal.
# mifuncion recibe un número "n" y DEVUELVE una nueva función (la lambda)
# que multiplica cualquier valor "a" por ese "n".
def mifuncion(n):
    return lambda a : a * n  # la lambda "recuerda" el valor de n (esto se llama closure)

# Creamos dos funciones distintas a partir de la misma plantilla:
duplicador = mifuncion(2)   # duplicador ahora es: lambda a : a * 2
triplicador = mifuncion(3)  # triplicador ahora es: lambda a : a * 3

# Llamamos a las funciones generadas como cualquier otra función
print(duplicador(5)) # 5 * 2 = 10
print(triplicador(5)) # 5 * 3 = 15


