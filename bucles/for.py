# ============================================================
# BUCLE FOR
# ============================================================
# Un bucle "for" sirve para REPETIR código una vez por cada elemento
# de una colección (un texto, una lista, un rango de números, etc.).
#
# Estructura:
#   for variable in coleccion:
#       código que se repite
#
# En cada vuelta, "variable" toma el valor del siguiente elemento.
# ============================================================


# ------------------------------------------------------------
# 1. Recorrer un texto (string) letra por letra
# ------------------------------------------------------------
# Un texto es una secuencia de caracteres, así que "for" puede recorrerlo.
palabra = "Python"

# En cada vuelta, "letra" vale una letra distinta: P, y, t, h, o, n
for letra in palabra:
    print(letra)  # Imprime cada letra en una línea distinta

print("-------------------------")  # Solo una línea separadora para ver mejor la salida

# ------------------------------------------------------------
# 2. Bucles anidados (un for dentro de otro for)
# ------------------------------------------------------------
# Las listas se escriben entre corchetes [] y separan sus elementos con comas.
adjetivos = ["Rica", "Saludable"]
frutas = ["Manzana", "Naranja", "Kiwi"]

# El for de AFUERA recorre los adjetivos.
# Por CADA adjetivo, el for de ADENTRO recorre TODAS las frutas.
# Total de vueltas: 2 adjetivos x 3 frutas = 6 impresiones.
for adjetivo in adjetivos:
    for fruta in frutas:
        print(fruta, adjetivo)  # print con coma separa los valores con un espacio

# Resultado (primero todas con "Rica", luego todas con "Saludable"):
# Manzana Rica
# Naranja Rica
# Kiwi Rica
# Manzana Saludable
# Naranja Saludable
# Kiwi Saludable

print("-------------------------")  # Solo una línea separadora para ver mejor la salida

# ------------------------------------------------------------
# 3. "continue" y "else" en un for (ejemplo comentado)
# ------------------------------------------------------------
# - "continue" salta el resto del código de ESA vuelta y pasa a la siguiente.
#   Aquí, cuando la fruta es "Naranja", no se imprime.
# - El "else" de un for se ejecuta cuando el bucle termina todas sus vueltas
#   (solo se omite si el bucle se detiene con "break").
# Para probarlo, quita los "#" del inicio de cada línea.
#
for fruta in frutas:
    if fruta == "Naranja":
        continue
    print(fruta)
else:
    print("Ya hemos terminado el bucle for")
#
# Resultado:
# Manzana
# Kiwi
# Ya hemos terminado el bucle for


print("-------------------------")  # Solo una línea separadora para ver mejor la salida


# 3. "Break" y "else" en un for (ejemplo comentado)
# ------------------------------------------------------------
# - "Break" termina el codigo del for y se salta el else

for fruta in frutas:
    if fruta == "Naranja":
        break
    print(fruta)
else:
    print("Ya hemos terminado el bucle for")
#
# Resultado:
# Manzana


print("-------------------------")  # Solo una línea separadora para ver mejor la salida

# ------------------------------------------------------------
# 4. range(): generar secuencias de números
# ------------------------------------------------------------
# range() crea una secuencia de números para repetir algo cierta cantidad de veces.
# El número final NUNCA se incluye.

# range(fin): comienza en 0 y termina ANTES de "fin".
# Imprime: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
for i in range(10):
    print(i)

print("-------------------------")  # Solo una línea separadora para ver mejor la salida

# range(inicio, fin): comienza en "inicio" y termina ANTES de "fin".

for i in range(3,5):
    print(i) # Imprime: 3, 4

print("-------------------------")  # Solo una línea separadora para ver mejor la salida

# range(inicio, fin, paso): "paso" indica de cuánto en cuánto avanza.

for i in range(0,11,2): # Imprime los pares del 0 al 10: 0, 2, 4, 6, 8, 10
    print(i)

print("-------------------------")  # Solo una línea separadora para ver mejor la salida


# ------------------------------------------------------------
# 5. "pass": no hacer nada
# ------------------------------------------------------------
# Python no permite un bucle vacío. "pass" es una instrucción que no hace nada
# y sirve como "relleno" cuando todavía no sabes qué código poner.
# Este bucle da 10 vueltas, pero no hace nada en ninguna.

for i in range(10):
    pass
