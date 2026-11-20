# ============================================================
# OPERADORES DE COMPARACIÓN
# ============================================================
# Sirven para COMPARAR dos valores.
# El resultado SIEMPRE es un Boolean (booleano)
#   True  -> Verdadero (la comparación se cumple)
#   False -> Falso     (la comparación NO se cumple)

x = 5
y = 3
z = 5

# ==  (igual a): pregunta si los dos valores son IGUALES.
# OJO: se usan DOS signos "==". Un solo "=" sirve para asignar

print(x == y)  # ¿5 es igual a 3?          -> False

# !=  (distinto de): pregunta si los valores son DIFERENTES.
print(x != y)  # ¿5 es distinto de 3?      -> True

print(x > z)   # ¿5 es mayor que 5?-> False (son iguales, no mayor)
print(x < y)   # ¿5 es menor que 3?        -> False
print(x >= z)  # ¿5 es mayor o igual a 5?  -> True (porque son iguales)
print(x <= y)  # ¿5 es menor o igual a 3?  -> False


# ============================================================
# OPERADORES LÓGICOS
# ============================================================
# Sirven para COMBINAR varias comparaciones (o valores booleanos)
# en una sola. También devuelven True o False.

# and  (y): devuelve True SOLO si AMBAS condiciones son True.
#           Si al menos una es False, el resultado es False.
#
#   True  and True  -> True
#   True  and False -> False
#   False and True  -> False
#   False and False -> False

#      x > y -> True     y > z -> False
print(x > y and y > z)  # True and False -> False

# or  (o): devuelve True si AL MENOS UNA de las condiciones es True.
#          Solo da False cuando AMBAS son False.
#
#   True  or True  -> True
#   True  or False -> True
#   False or True  -> True
#   False or False -> False
#
#      x > y -> True    y > z -> False
print(x > y or y > z)   # True or False -> True

# not  (no): INVIERTE el valor booleano.
#            Lo que es True se vuelve False, y lo que es False se vuelve True.
print(not v)  # not True  -> False
print(not f)  # not False -> True
# Nota: los paréntesis en not(v) también funcionan, pero no son necesarios,
# porque "not" es un operador, no una función.


# Guardamos valores booleanos directamente en variables.
# Nota: True y False se escriben con la primera letra en MAYÚSCULA.

v = True   # v de "verdadero"
f = False  # f de "falso"

