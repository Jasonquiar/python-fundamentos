# ============================================================
# MATCH - CASE (Coincidencia de patrones)
# ============================================================
# "match" sirve para comparar UNA variable contra varios valores
# posibles y ejecutar el código del caso que coincida.
# Es parecido a escribir muchos if / elif / else, pero más ordenado
# y fácil de leer cuando hay muchas opciones.
# Está disponible desde Python 3.10 en adelante.
# ============================================================

# Creamos una variable llamada "dia" y le guardamos el número 4.
# Cambia este número (1, 2, 3, 4...) para ver cómo cambia el resultado.
dia = 4

# "match" toma el valor de "dia" y lo va comparando con cada "case",
# de arriba hacia abajo, hasta encontrar uno que coincida.
match dia:
    # Si dia es igual a 1, se ejecuta esta línea.
    case 1:
        print("Hoy es Lunes")
    # Si dia es igual a 2, se ejecuta esta línea.
    case 2:
        print("Hoy es Martes")
    # Si dia es igual a 3, se ejecuta esta línea.
    case 3:
        print("Hoy es Miércoles")
    # El guion bajo "_" es el caso "comodín": atrapa CUALQUIER valor
    # que no coincidió con los casos anteriores.
    # Funciona igual que el "else" en un if / elif / else.
    case _:
        print("No coincide con ninguna de las anteriores")

# Importante:
# - Solo se ejecuta UN caso: el primero que coincida. Los demás se ignoran.
# - La indentación (los espacios al inicio) es obligatoria en Python:
#   los "case" van dentro del "match", y el código va dentro de cada "case".
# - Como dia = 4 y no hay "case 4", el programa imprime:
#   "No coincide con ninguna de las anteriores"
#
# Equivalente usando if / elif / else:
# if dia == 1:
#     print("Hoy es Lunes")
# elif dia == 2:
#     print("Hoy es Martes")
# elif dia == 3:
#     print("Hoy es Miércoles")
# else:
#     print("No coincide con ninguna de las anteriores")
