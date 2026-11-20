# =====================================================================
# CONDICIONALES EN PYTHON: if, elif, else
# ---------------------------------------------------------------------
# Los condicionales permiten que el programa "tome decisiones":
# ejecuta un bloque de código SOLO si una condición es verdadera (True).
#
#   if condicion:        -> "si" se cumple esta condición, haz esto
#   elif otra_condicion: -> "si no, pero si" se cumple esta otra, haz esto
#   else:                -> "si no" se cumplió ninguna de las anteriores, haz esto
#
# Reglas importantes:
#   - Después de cada condición se escriben dos puntos ":".
#   - El código que pertenece a cada bloque va con SANGRÍA (4 espacios).
#     Python usa la sangría para saber qué líneas están "dentro" del if.
#   - Python revisa las condiciones de arriba hacia abajo y ejecuta
#     SOLO el primer bloque cuya condición sea True; el resto se ignora.
#   - Puedes tener varios elif, pero solo un if al inicio y un else al final.
# =====================================================================


# ---------------------------------------------------------------------
# EJEMPLO 1: if / elif / else con el operador lógico "or"
# ---------------------------------------------------------------------
x = 5
y = 3
z = 10

# "or" (o) devuelve True si AL MENOS UNA de las dos condiciones es verdadera.
#   x > y  -> 5 > 3  -> True
#   x > z  -> 5 > 10 -> False
#   True or False    -> True   => entra a este bloque

if x > y or x > z:
    print("x es mayor a y O x es mayor a z") 

# elif solo se revisa si la condición del if anterior fue False.
# "==" compara si dos valores son iguales (no confundir con "=", que asigna).
elif x == y:
    print("x es igual a y")

# else se ejecuta cuando NINGUNA de las condiciones anteriores fue True.
# No lleva condición, solo los dos puntos.
else:
    print("Ninguna de las condiciones anteriores se cumplió")


# ---------------------------------------------------------------------
# EJEMPLO 2: condicionales ANIDADOS (un if dentro de otro if)
# ---------------------------------------------------------------------
# También se pueden comparar textos (strings). La comparación distingue
# mayúsculas de minúsculas: "Python" no es igual a "python".
a = "Python"
b = "Javascript"
c = "Python"

# Primero se evalúa el if "externo": ¿a es igual a c?
#   "Python" == "Python" -> True  => entramos al bloque
if a == c:
    # Ahora, ya DENTRO del if externo, evaluamos un if "interno".
    # Fíjate en la sangría extra: este bloque pertenece al if de arriba.
    # ¿a es igual a b?  "Python" == "Javascript" -> False,  asi que se lo salta
    
    if a == b:
        print("a es igual a b pero es distinto a c")
    # 👇 Como a == b fue False, se ejecuta el else del if INTERNO .
    else:
        print("a y c son iguales y ya estoy saliendo por el else del if interno") # Este es el mensaje que verás al correr el programa.

# 👇 Este else pertenece al if EXTERNO (está al mismo nivel de sangría).
# Solo se ejecutaría si a fuera distinto de c.
else:
    print("a no es igual a c")


# ---------------------------------------------------------------------
# EJEMPLO 3: la palabra clave "pass"
# ---------------------------------------------------------------------
e = 10
f = 10

# Python NO permite un bloque vacío: después de "if ...:" debe haber
# al menos una línea con sangría, o dará error (IndentationError).
# "pass" es una instrucción que no hace nada; sirve como "marcador de
# lugar" cuando todavía no sabes qué código poner ahí.
# Aquí e == f es True, pero como solo hay "pass", no se imprime nada.
if e == f:
    pass  # Para ignorar la estructura if hasta tanto definamos que comportamiento se espera
