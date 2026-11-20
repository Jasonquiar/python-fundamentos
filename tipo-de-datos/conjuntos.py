# ============================================================
# CONJUNTOS (set)
# ============================================================
# Un conjunto guarda VARIOS valores en una sola variable.
# Se escribe entre llaves {} y los elementos se separan con comas.
#
# Características:
# - NO ordenados: los elementos no tienen posición fija.
#   Por eso NO se puede usar índice (frutas[0] da ERROR)
#   y al imprimirlos el orden puede salir distinto cada vez.
# - Elementos ÚNICOS: no permite duplicados. Si repites un valor,
#   Python lo guarda una sola vez.
# - Modificables: puedes agregar y quitar elementos.
#
# Comparación rápida:
#   Lista  [] -> ordenada, modificable, permite duplicados
#   Tupla  () -> ordenada, NO modificable, permite duplicados
#   Set    {} -> NO ordenado, modificable, SIN duplicados
# ============================================================


# ------------------------------------------------------------
# 1. Crear un conjunto
# ------------------------------------------------------------
# "Naranja" está escrita dos veces, pero el set solo la guarda una vez.
frutas = {"Manzana", "Naranja", "Mandarina", "Naranja"}
print(frutas)        # {'Manzana', 'Naranja', 'Mandarina'}  (el orden puede variar)
print(type(frutas))  # <class 'set'>
print(len(frutas))   # 3  -> no 4, porque el duplicado se eliminó


# ------------------------------------------------------------
# 2. Saber si un elemento está (o no está) en el conjunto
# ------------------------------------------------------------
print("Manzana" in frutas)   # True  -> "Manzana" SÍ está
print("Pera" not in frutas)  # True  -> es verdad que "Pera" NO está


# ------------------------------------------------------------
# 3. Agregar elementos
# ------------------------------------------------------------

# add(valor): agrega UN solo elemento.
frutas.add("Pera")
print(frutas)  # Ahora también tiene 'Pera'

# update(coleccion): agrega VARIOS elementos de una vez.
# Acepta listas, tuplas u otros conjuntos.
frutasTropicales = { "Piña", "Mango"}
frutas.update(frutasTropicales)
print(frutas)  # Ahora también tiene 'Piña' y 'Mango'


# ------------------------------------------------------------
# 4. Eliminar elementos
# ------------------------------------------------------------

# remove(valor): elimina ese elemento.
# OJO: si el elemento NO existe, da ERROR (KeyError).
frutas.remove("Mango")
print(frutas)  # Ya no tiene 'Mango'

# discard(valor): también elimina ese elemento,
# pero si NO existe, no pasa nada (no da error).
# Aquí "Banana" no está en el conjunto, y aun así el programa sigue sin problema.
frutas.discard("Banana")
print(frutas)  # Queda igual que antes

# pop(): elimina UN elemento cualquiera.
# Como el conjunto no tiene orden, no sabemos cuál va a eliminar.
frutas.pop()
print(frutas)  # Tiene un elemento menos (puede ser cualquiera)

# clear(): vacía el conjunto por completo.
frutas.clear()
print(frutas)  # set()  -> así se muestra un conjunto vacío


# ------------------------------------------------------------
# 5. Mezclar tipos y recorrer con for (ejemplo comentado)
# ------------------------------------------------------------
# Un conjunto también puede tener texto, números y booleanos.
# Con "for" lo recorres igual que una lista, pero el orden no está garantizado.
# Para probarlo, quita los "#" del inicio de cada línea.
#
# CUIDADO con este ejemplo: Python considera que True es igual a 1.
# Si el conjunto tuviera 1 y True juntos, solo guardaría uno de los dos.

conjuntos = {"Python", 156, True}
print(conjuntos)
print(type(conjuntos))

for item in conjuntos:
    print(item) # La salida no tiene orden

print("--------------")  # Línea separadora para ver mejor la salida


# ------------------------------------------------------------
# 6. Operaciones de conjuntos (como en matemáticas)
# ------------------------------------------------------------
a = {"a", "b", "c"}
b = {"c", "d", "e"}
# El único elemento que tienen en común es "c".

# union(): TODOS los elementos de ambos conjuntos, sin repetir.
u = a.union(b)

print(u)  # {'a', 'b', 'c', 'd', 'e'}  (el orden puede variar)

# intersection(): solo los elementos que están en LOS DOS conjuntos.
i = a.intersection(b)

print(i)  # {'c'}

# difference(): los elementos que están en "a" pero NO en "b".
d = a.difference(b)

print(d)  # {'a', 'b'}  (el orden puede variar)
