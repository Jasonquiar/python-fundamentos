
# open(nombre, modo)

# r (read) Lectura
# w (write) Escritura
# x (Crea archivo nuevo)
# a (append) Agrega al final del archivo sin borrar lo que ya tiene
# Ojo: "w" BORRA todo el contenido anterior; "x" da error si el archivo ya existe

# "with" abre el archivo y lo CIERRA automáticamente al terminar el bloque,
# así no tenemos que llamar f.close() nosotros mismos.

# f = open("archivo.txt", "r")
# print(f.readline())
# f.close()

# encoding="utf-8" permite leer bien tildes y la ñ.
# Nota: "archivo.txt" se busca en la carpeta desde donde ejecutas el programa.

# Bloque 1: leer el archivo
try:
    with open("archivo.txt", "r", encoding="utf-8") as f:
        print(f.readline())  # readline() lee UNA línea (la primera)
        print(f.readline())  # la siguiente llamada lee la segunda línea
except FileNotFoundError:
    # Si el archivo no existe, lo creamos vacío con el modo "x"
    open("archivo.txt", "x") # Con la "x" se crea el archivo
    print("No se ha encontrado el archivo")

# Bloque 2: agregar texto y luego leer todo el archivo
try:
    # Modo "a": escribe al final, conservando lo que ya había
    with open("archivo.txt", "a") as f:
        f.write("\n")  # salto de línea para que el texto nuevo quede en otra línea
        f.write("Hola mundo desde write en el with")
    # Volvemos a abrirlo en modo lectura para ver el resultado
    with open("archivo.txt", "r", encoding="utf-8") as f:
        print(f.read())  # read() lee TODO el contenido de una vez
except FileNotFoundError:
    print("No se ha encontrado el archivo")
