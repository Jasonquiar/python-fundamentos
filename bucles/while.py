# ---------------------------------------------------------------
# BUCLE WHILE ("mientras")
# Repite un bloque de instrucciones MIENTRAS una condición sea
# verdadera (True). En cuanto la condición se vuelve falsa (False),
# el bucle se detiene.
#
# Estructura básica:
#     while condicion:
#         instrucciones que se repiten
# ---------------------------------------------------------------
# EJEMPLO
# ---------------------------------------------------------------
# Contexto:
# Queremos crear una lista del 1 al 10 sin el numero 5 y otra que sea del 1 al 4 pero sin el 5
# 1 2 3 4 6 7 8 9 10
# 1 2 3 4 

# Creamos una variable "contador" que empieza en 0.
# Ella decide cuántas veces se repite el bucle.
i = 0

# "¿i es menor que 10?" -> si es True, entra al bucle; si es False, sale.
while i < 10:
    # Sumamos 1 a i en cada vuelta. "i += 1" es lo mismo que "i = i + 1".
    # ¡Importante! Si olvidamos esta línea, i nunca cambia, y creamos un BUCLE INFINITO.
    i += 1

    # OJO: Para cambiar el resultaro haz "continue" un comentario
    if i == 5:
        # "continue" salta el resto del código de ESTA vuelta
        # (no llega al print) y vuelve directo a revisar la condición.
        
        continue # -> Resultado: 1 2 3 4 6 7 8 9 10 i dejo de ser menor que 10
        
        # "break" nos saca totalmente del bucle 
        break # -> Resultado 1 2 3 4 

    # Mostramos el valor actual de i en pantalla.
    print(i)

# El "else" de un while es opcional y se ejecuta UNA sola vez,
# cuando la condición del while se vuelve falsa (aquí, cuando i llega a 10).
# Ojo: si el bucle se interrumpe con "break", este else NO se ejecuta.
else:
    print("i dejó de ser menor a 10")

