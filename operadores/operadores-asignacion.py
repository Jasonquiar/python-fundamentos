# Operadores Asignación
# Sirven para asignar valores a las variables y realizar operaciones matemáticas al mismo tiempo.
x = 5
x += 3 # Suma
x -= 3 # Resta
x *= 3 # Multiplicación
x /= 3 # División
x %= 2 # Módulo(resto)

y = 20

y //= 2 # División Entera Imprime 10, porque 20 dividido entre 2 es 10.
y **= 3 # Exponente 10 * 10 * 10 Imprime 1000, porque 10 elevado a la potencia de 3 es 1000.

# WALRUS (morsa) := ( En ingles significa Morza)
# WALRUS es un operador de asignación que se introdujo en Python 3.8. 
# Nos permite asignar directamente dentro de un metodo una variable
print(z := 3) # Imprime 3, porque estamos asignando el valor 3 a la variable z y al mismo tiempo devolviendo ese valor.
print(z) # Imprime 3