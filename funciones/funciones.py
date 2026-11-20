# ============================================================
# FUNCIONES
# ============================================================
# Una función es un bloque de código con nombre que SOLO se ejecuta
# cuando la llamamos.
#
# ¿Para qué sirven?
# - Organizar el código en partes pequeñas.
# - Reutilizar: escribes el código una vez y lo usas muchas veces.
#
# Estructura:
#   def nombre_funcion(parametros):
#       código de la función
#
# - "def" le dice a Python que vamos a DEFINIR (crear) una función.
# - El código de adentro debe ir con sangría (indentación).
# - Definir la función NO la ejecuta. Para ejecutarla hay que LLAMARLA:
#   nombre_funcion(argumentos)
# ============================================================


# ------------------------------------------------------------
# 1. Función con parámetros y un valor por defecto
# ------------------------------------------------------------
# PARÁMETROS: son las variables que pones en el "def" (aquí: nombre y nacionalidad).
#   Funcionan como "espacios vacíos" que se llenan cuando llamas la función.
#
# Valor por defecto: nacionalidad="Colombia" significa que si NO le pasas
#   una nacionalidad, usará "Colombia" automáticamente.
def saludar(nombre, nacionalidad="Colombia"):
    print("Hola", nombre,"de", nacionalidad)

# ARGUMENTOS: son los valores reales que le pasas al LLAMAR la función.
# Se asignan en orden: el primero va a "nombre", el segundo a "nacionalidad".

saludar("Pedro", "España")  # Hola Pedro de España    -> usa la nacionalidad que le pasamos
saludar("María")            # Hola María de Colombia  -> usa el valor por defecto
saludar("Ana")              # Hola Ana de Colombia    -> usa el valor por defecto


# ------------------------------------------------------------
# 2. Función que DEVUELVE un valor con "return"
# ------------------------------------------------------------
# "return" entrega un resultado a quien llamó la función,
# para que se pueda guardar en una variable y usar después.
# (print solo MUESTRA en pantalla; return DEVUELVE el valor.)
def sumar(a,b):
    return a + b


# Llamamos a sumar con los argumentos 2 y 3 -> a = 2, b = 3.
# La función devuelve 5, y ese 5 se guarda en "resultado".
resultado = sumar(2,3)
print(resultado)  # 5


# ------------------------------------------------------------
# 3. Función vacía con "pass"
# ------------------------------------------------------------
# Python no permite una función sin código adentro.
# "pass" no hace nada: sirve de relleno cuando aún no sabes qué poner.
def funcion():
    pass
