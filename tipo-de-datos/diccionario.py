# ============================================================
# DICCIONARIOS (dict)
# ============================================================
# Un diccionario guarda datos en pares CLAVE : VALOR.
# Es como un diccionario de verdad: buscas una palabra (la clave)
# y obtienes su significado (el valor).
#
# Se escribe entre llaves {} así:  {"clave": valor, "otra_clave": otro_valor}
#
# Características:
# - En vez de usar índices (0, 1, 2...), accedes a los datos por su CLAVE.
# - Ordenados: desde Python 3.7 mantienen el orden en que agregas los datos.
# - Modificables: puedes cambiar, agregar y quitar pares.
# - Las claves NO se repiten: si usas una clave que ya existe,
#   se reemplaza su valor.
# ============================================================


# ------------------------------------------------------------
# 1. Crear un diccionario
# ------------------------------------------------------------
# Cada línea es un par:  "clave": valor
auto = {
    "marca": "Renault",   # clave "marca"  -> valor "Renault"
    "modelo": "Clio",     # clave "modelo" -> valor "Clio"
    "año": 2025           # clave "año"    -> valor 2025
}

print(auto)  # {'marca': 'Renault', 'modelo': 'Clio', 'año': 2025}


# ------------------------------------------------------------
# 2. Leer un valor usando su clave
# ------------------------------------------------------------
# Forma 1: con corchetes. Si la clave NO existe, da ERROR (KeyError).
print(auto["marca"])      # Renault

# Forma 2: con get(). Si la clave NO existe, devuelve None (no da error).
print(auto.get("marca"))  # Renault


# ------------------------------------------------------------
# 3. Ver todas las claves o todos los valores
# ------------------------------------------------------------
print(auto.keys())    # dict_keys(['marca', 'modelo', 'año'])
print(auto.values())  # dict_values(['Renault', 'Clio', 2025])


# ------------------------------------------------------------
# 4. Saber si una clave existe
# ------------------------------------------------------------
# "in" busca entre las CLAVES (no entre los valores).
if "marca" in auto:
    print("Marca es una de las propiedades de este diccionario")


# ------------------------------------------------------------
# 5. Modificar y agregar datos
# ------------------------------------------------------------
# Si la clave YA existe, se cambia su valor.
auto["año"] = 2020
print(auto)  # {'marca': 'Renault', 'modelo': 'Clio', 'año': 2020}

# Si la clave NO existe, se agrega un par nuevo al final.
auto["color"] = "Verde"
print(auto)  # {'marca': 'Renault', 'modelo': 'Clio', 'año': 2020, 'color': 'Verde'}

# update(): cambia o agrega VARIOS pares de una vez.
# "año" ya existía -> se cambia a 2022.  "puertas" no existía -> se agrega.
auto.update({"año": 2022, "puertas": 4})
print(auto)  # {'marca': 'Renault', 'modelo': 'Clio', 'año': 2022, 'color': 'Verde', 'puertas': 4}


# ------------------------------------------------------------
# 6. Eliminar datos (ejemplos comentados)
# ------------------------------------------------------------
# Para probarlos, quita los "#" del inicio de las líneas.

# pop(clave): # elimina el par con ESA clave.
# auto.pop("puertas")
# print(auto)

# popitem(): # elimina el ÚLTIMO par que se agregó a la biblioteca.
# auto.popitem()
# print(auto)

# clear(): # vacía el diccionario por completo -> {}
# auto.clear()
# print(auto)


# ------------------------------------------------------------
# 7. Recorrer un diccionario con for
# ------------------------------------------------------------
# Forma 1: recorrer directamente el diccionario -> obtienes las CLAVES.
for k in auto:  # k = key (clave)
    print(k)    # marca, modelo, año, color, puertas

print("---")  # Línea separadora

# Forma 2: con values() -> obtienes los VALORES.
for v in auto.values():  # v = value (valor)
    print(v)             # Renault, Clio, 2022, Verde, 4

print("---")  # Línea separadora

# Forma 3: con items() -> obtienes CLAVE y VALOR al mismo tiempo.
# Cada par se "desempaqueta" en dos variables: k y v.
for k,v in auto.items(): # v = value k = Key
    print(k,v)  # marca Renault, modelo Clio, año 2022, ...


# ------------------------------------------------------------
# 8. Diccionarios anidados (un diccionario dentro de otro)
# ------------------------------------------------------------
# El valor de cada clave ("hijo1", "hijo2", "hijo3") es OTRO diccionario.
familia = {
    "hijo1" : {
        "nombre": "Pedro",
        "edad": 8
    },
    "hijo2" : {
        "nombre": "Ana",
        "edad": 7
    },
    "hijo3" : {
        "nombre": "Marcelo",
        "edad": 6
    }
}
print(familia)
# Para llegar a un dato interno se encadenan los corchetes:
# familia["hijo1"]            -> {'nombre': 'Pedro', 'edad': 8}
# familia["hijo1"]["nombre"]  -> 'Pedro'
print(familia["hijo1"]["nombre"])  # Pedro
