# Importamos funciones específicas desde nuestro módulo operaciones.py
# Sintaxis: from nombre_del_modulo import funcion1, funcion2, ...
# El nombre del módulo es el nombre del archivo SIN la extensión .py
# Nota: ambos archivos deben estar en la misma carpeta para que el import funcione
from operaciones import sumar, restar, multiplicar, dividir

# Otra forma sería: import operaciones  -> y usar operaciones.sumar(2,3)

# Ahora podemos usar las funciones como si estuvieran definidas en este archivo
print(sumar(2,3))        # 2 + 3 = 5
print(restar(2,3))       # 2 - 3 = -1
print(multiplicar(2,3))  # 2 * 3 = 6
print(dividir(10,5))     # 10 / 5 = 2.0 (la división siempre devuelve float)
