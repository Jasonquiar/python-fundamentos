# ============================================================
# TUPLAS
# ============================================================
# Una tupla guarda VARIOS valores en una sola variable, igual que una lista.
# Se escribe entre paréntesis () y los elementos se separan con comas.
#
# Características:
# - Ordenadas: cada elemento tiene una posición fija (índice).
# - INMUTABLES: una vez creada, NO se puede cambiar, agregar ni quitar nada.
#   (Esta es la gran diferencia con las listas.)
# - Permiten duplicados: el mismo valor puede aparecer varias veces.
#
# ¿Cuándo usarlas? Cuando tienes datos que no deberían cambiar,
# por ejemplo: coordenadas, días de la semana, colores fijos, etc.
# ============================================================


# ------------------------------------------------------------
# 1. Crear una tupla y leer sus elementos
# ------------------------------------------------------------
# El índice empieza en 0, igual que en las listas.
# Indice         0           1           2      3
tecnologias = ("Python", "Javascript", "Go", "Python")  # "Python" repetido (duplicado permitido)

print(tecnologias)     # ('Python', 'Javascript', 'Go', 'Python')
print(tecnologias[1])  # Javascript  -> tupla[indice] sirve para LEER un elemento

print(len(tecnologias))  # 4  -> len() cuenta cuántos elementos hay

print(type(tecnologias))  # <class 'tuple'>

# OJO: esto daría ERROR, porque las tuplas no se pueden modificar:
# tecnologias[1] = "Java"   -> TypeError


# ------------------------------------------------------------
# 2. Tupla de UN solo elemento: ¡lleva coma!
# ------------------------------------------------------------
# Si escribes ("Manzana") sin coma, Python lo ve como un texto normal (str).
# La coma final es lo que le dice a Python que es una tupla.
fruta = ("Manzana",)

print(type(fruta))  # <class 'tuple'>


# ------------------------------------------------------------
# 3. Una tupla puede mezclar tipos de datos
# ------------------------------------------------------------
tupla = ("Python", 5, True)  # texto (str), número (int) y booleano (bool)

print(tupla)        # ('Python', 5, True)
print(type(tupla))  # <class 'tuple'>


# ------------------------------------------------------------
# 4. Desempaquetar una tupla
# ------------------------------------------------------------
# Guarda cada elemento de la tupla en su propia variable, en orden.
# Debe haber TANTAS variables como elementos (aquí 3 y 3).
# Asi onemos la informacion de la tupla dentro de las variables declaradas
x, y, z = tupla
print(x)  # Python
print(y)  # 5
print(z)  # True


# ------------------------------------------------------------
# 5. Unir tuplas con "+"
# ------------------------------------------------------------
# No modifica las tuplas originales: crea una tupla NUEVA.
tupla1 = (1,2,3)
tupla2 = (3,4,5)
tupla3 = tupla1 + tupla2

print(tupla3)  # (1, 2, 3, 3, 4, 5)  -> el 3 aparece dos veces porque está en ambas


# ------------------------------------------------------------
# 6. Repetir una tupla con "*"
# ------------------------------------------------------------
tupla = ("Python", 5, True)

print(tupla * 2)  # ('Python', 5, True, 'Python', 5, True)


# ------------------------------------------------------------
# 7. Recorrer una tupla con for
# ------------------------------------------------------------
# Igual que con las listas: en cada vuelta "item" toma el siguiente elemento.
for item in tupla:
    print(item)  # Python, luego 5, luego True (cada uno en una línea)

print("---------------")  # Línea separadora para ver mejor la salida


# ------------------------------------------------------------
# 8. "Truco" para modificar una tupla
# ------------------------------------------------------------
# se hace Casteando con el medodo "List" o "Tuple"
# Como la tupla no se puede cambiar, hacemos esto:
#   1) Convertirla en lista con list()
#   2) Modificar la lista (que sí se puede)
#   3) Convertirla de nuevo en tupla con tuple()
# En realidad no cambiamos la tupla original: creamos una NUEVA
# y la guardamos en la misma variable.
tuplaAModificar = ("Python", "Javascript", "Go")
listaComodin = list(tuplaAModificar)   # Paso 1: ['Python', 'Javascript', 'Go']
listaComodin.append("ReactJS")         # Paso 2: ['Python', 'Javascript', 'Go', 'ReactJS']
tuplaAModificar = tuple(listaComodin)  # Paso 3: de vuelta a tupla

print(tuplaAModificar)  # ('Python', 'Javascript', 'Go', 'ReactJS')
