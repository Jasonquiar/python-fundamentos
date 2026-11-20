# ============================================================
# LISTAS
# ============================================================
# Una lista guarda VARIOS valores dentro de una sola variable.
# Se escribe entre corchetes [] y los elementos se separan con comas.
#
# Características:
# - Ordenadas: cada elemento tiene una posición fija (índice).
# - Modificables: puedes cambiar, agregar o quitar elementos.
# - Permiten duplicados: el mismo valor puede aparecer varias veces.
# ============================================================


# ------------------------------------------------------------
# 1. Crear una lista e índices
# ------------------------------------------------------------
# El ÍNDICE es la posición de cada elemento. ¡Empieza en 0, no en 1!

# Índices:   0          1           2            3
frutas = ["Manzana", "Naranja", "Mandarina", "Naranja"]  # "Naranja" está repetida (duplicado permitido)
print(frutas)        # ['Manzana', 'Naranja', 'Mandarina', 'Naranja']
print(type(frutas))  # <class 'list'>  -> type() nos dice el tipo de dato


# ------------------------------------------------------------
# 2. Modificar un elemento
# ------------------------------------------------------------
# lista[indice] = nuevo_valor  -> reemplaza el elemento de esa posición.
# Aquí cambiamos "Naranja" (índice 1) por "Banana".
frutas[1] = "Banana"

print(frutas[1])  # Banana  -> lista[indice] sirve para LEER un elemento
print(frutas)     # ['Manzana', 'Banana', 'Mandarina', 'Naranja']


# ------------------------------------------------------------
# 3. Una lista puede mezclar tipos de datos
# ------------------------------------------------------------
# Esta lista tiene un texto (str), un número (int) y un booleano (bool).
lista = ["Sergie Code", 5, True]
print(lista)        # ['Sergie Code', 5, True]
print(type(lista))  # <class 'list'>


# ------------------------------------------------------------
# 4. len(): cantidad de elementos
# ------------------------------------------------------------
print(len(lista))   # 3
print(len(frutas))  # 4


# ------------------------------------------------------------
# 5. Slicing (rebanar): obtener una parte de la lista
# ------------------------------------------------------------
# lista[inicio:fin] -> desde "inicio" hasta ANTES de "fin".
# Si no pones "fin" (como aquí), llega hasta el final.
# frutas[1:] = desde el índice 1 hasta el final.
print(frutas[1:])  # ['Banana', 'Mandarina', 'Naranja']


# ------------------------------------------------------------
# 6. "in": saber si un elemento está en la lista
# ------------------------------------------------------------
# "in" devuelve True si el elemento existe y False si no.
if "Manzana" in frutas:
    print("La manzana está dentro de las frutas")


# ------------------------------------------------------------
# 7. Métodos de las listas
# ------------------------------------------------------------
# Un MÉTODO es una función que pertenece a la lista y se usa con un punto:
#   lista.metodo()
# Estos métodos MODIFICAN la lista original.

# Indices      0        1       2
vehiculos = ["Auto", "Moto", "Avión"]

# append(valor): agrega un elemento AL FINAL de la lista.
vehiculos.append("Barco")  # "Barco" queda en el índice 3
print(vehiculos)  # ['Auto', 'Moto', 'Avión', 'Barco']

# insert(indice, valor): agrega un elemento EN LA POSICIÓN que elijas.
# Los elementos que estaban desde esa posición se corren a la derecha.
vehiculos.insert(1, "Bicicleta")
print(vehiculos)  # ['Auto', 'Bicicleta', 'Moto', 'Avión', 'Barco']

# remove(valor): elimina el elemento que tenga ESE VALOR.
# (Si el valor está repetido, solo borra el primero que encuentre.)
vehiculos.remove("Auto")
print(vehiculos)  # ['Bicicleta', 'Moto', 'Avión', 'Barco']

# pop(indice): elimina el elemento que está en ESA POSICIÓN.
# Si no le das índice, elimina el último.
vehiculos.pop(1)  # Borra el índice 1, que ahora es "Moto"
print(vehiculos)  # ['Bicicleta', 'Avión', 'Barco']

# sort(): ordena la lista (alfabéticamente si son textos, de menor a mayor si son números).
vehiculos.sort()
print(vehiculos)  # ['Avión', 'Barco', 'Bicicleta']

# reverse(): invierte el orden de la lista (el último pasa a ser el primero).
vehiculos.reverse()
print(vehiculos)  # ['Bicicleta', 'Barco', 'Avión']


# ------------------------------------------------------------
# 8. Unir listas
# ------------------------------------------------------------
coleccion1 = [1,2,3]
coleccion2 = [4,5,6]

# Forma 1: con el operador "+"
# Crea una lista NUEVA. coleccion1 y coleccion2 no cambian.
coleccion3 = coleccion1 + coleccion2
print(coleccion3)  # [1, 2, 3, 4, 5, 6]

# Forma 2: con el método extend()
# NO crea una lista nueva: agrega los elementos de coleccion2 DENTRO de coleccion1.
coleccion1.extend(coleccion2)
print(coleccion1)  # [1, 2, 3, 4, 5, 6]
