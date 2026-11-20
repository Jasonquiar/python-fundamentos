# Operadores aritméticos

x = 5
y = 12

# Suma + 
print("Suma", x + y) # Imprime 17

# Resta -
print("Resta", x - y) # Imprime -7

# Multiplicación *
print("Multiplicación", x * y) # Imprime 60

# División / (retorna un float)
print("División", y / x) # Imprime 2.4


# Módulo %
# El operador módulo devuelve el resto de la división entre dos números.
print("Módulo(resto)", y % x) # Imprime 2, porque 12 dividido entre 5 es 2 con un resto de 2.

# Potencia **
print("Potencia", x ** x) # Imprime 3125, porque 5 elevado a la potencia de 5 es 3125.
# 5 * 5 * 5 * 5 * 5 = 3125

# División entera //
# La división entera se utiliza para obtener el cociente de una división sin el resto.
print("División Entera", y // x)


# Utilizando el operador módulo "%" para determinar si un número es par o impar
par = 7
print(par % 2 == 0) # Imprime False, porque 7 es impar y no es divisible entre 2.

par = 8
print(par % 2 == 0) # Imprime True, porque 8 es par


# Precedencia de operadores
# Este sera el orden conque Python evalua las operaciones, de mayor a menor precedencia:

# 1. Paréntesis - Ejemplo: ()
# 2. Exponentes - Ejemplo: **
# 3. Multiplicaciones, divisiones, divisiones enteras y restos -Ejemplo: *, /, //, %
# 4. Sumas y restas - Ejemplo: +, -
# 5. Comparaciones de identidad y pertenencia - Ejemplo: is, is not, in, not in
# 6. Lógicos - Ejemplo: and, or, not