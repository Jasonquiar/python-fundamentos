# try / except sirve para manejar errores (excepciones) sin que el programa se detenga.
# - try:     aquí va el código que PODRÍA fallar
# - except:  se ejecuta SOLO si ocurre el error indicado dentro del try
# - finally: se ejecuta SIEMPRE, haya error o no (útil para cerrar archivos, conexiones, etc.)

# Ejemplo 1: capturar una división entre cero
try:
    numero = 10 / 0  # esto lanza un ZeroDivisionError
except ZeroDivisionError:
    # En vez de que el programa se caiga, mostramos un mensaje amigable
    print("No se puede dividir por cero")

# Ejemplo 2: try / except / finally
x = 1

try:
    print(x)  # x sí existe, así que aquí NO hay error y se imprime 1
except NameError:
    # NameError ocurre cuando usamos una variable que no ha sido definida.
    # Prueba borrar "x = 1" para ver este mensaje.
    print("Esta variable no ha sido definida")
finally:
    # Este bloque se ejecuta siempre, falle o no el try
    print("Esto será ejecutado siendo exitoso o no el bloque")
